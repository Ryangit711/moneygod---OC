#!/usr/bin/env python3
"""
MT5 Trading Bot — Enhanced with Orchestrator Integration
Accepts trade_mode, bias, max_contracts from plumbing verdict.
Run via: python3 mt5_bot.py --mode paper --trade-mode REDUCED --bias NEUTRAL --max-contracts 1
"""

import argparse
import MetaTrader5 as mt5
import pandas as pd
import numpy as np
from datetime import datetime, time
import time as tm
import json
import os
import sys

# ==================== ARGUMENT PARSER ====================
def parse_args():
    parser = argparse.ArgumentParser(description="MT5 Trading Bot with Orchestrator Integration")
    parser.add_argument("--mode", choices=["paper", "live"], default="paper", help="Trading mode")
    parser.add_argument("--trade-mode", choices=["FULL", "NORMAL", "REDUCED", "FLAT"], default="NORMAL", help="Trade mode from plumbing verdict")
    parser.add_argument("--bias", choices=["BULLISH", "BEARISH", "NEUTRAL"], default="NEUTRAL", help="Directional bias from plumbing verdict")
    parser.add_argument("--max-contracts", type=int, default=1, help="Max contracts from position sizing")
    parser.add_argument("--symbol", default="BTCUSD", help="MT5 symbol")
    parser.add_argument("--config", default="mt5_config.json", help="Config file path")
    return parser.parse_args()

ARGS = parse_args()

# ==================== CONFIG ====================
def load_config(path: str) -> dict:
    default = {
        "symbol": ARGS.symbol,
        "timeframe": "H1",  # Will convert to mt5.TIMEFRAME_H1
        "lookback_bars": 500,
        "risk_pct": 1.0,
        "max_spread_pips": 50,
        "magic_number": 20260802,
        "comment": "AbhimanyuBot",
        "telegram_token": "",
        "telegram_chat_id": "",
        "log_file": "mt5_bot.log",
        "dry_run": ARGS.mode == "paper",
    }
    
    if os.path.exists(path):
        with open(path) as f:
            user_config = json.load(f)
            default.update(user_config)
    else:
        with open(path, "w") as f:
            json.dump(default, f, indent=2)
        print(f"Created default config at {path}")
    
    # Override with orchestrator args
    default["dry_run"] = ARGS.mode == "paper"
    default["trade_mode"] = ARGS.trade_mode
    default["bias"] = ARGS.bias
    default["max_contracts"] = ARGS.max_contracts
    
    # Apply trade-mode risk scaling (from plumbing-to-trade-bridge.md Decision Tree 4)
    risk_by_mode = {"FULL": 1.5, "NORMAL": 1.0, "REDUCED": 0.25, "FLAT": 0.0}
    default["risk_pct"] = risk_by_mode.get(ARGS.trade_mode, 1.0)
    
    return default

CONFIG = load_config(ARGS.config)

# ==================== TELEGRAM ALERTS ====================
def send_telegram(msg: str):
    if not CONFIG["telegram_token"] or not CONFIG["telegram_chat_id"]:
        return
    try:
        import requests
        url = f"https://api.telegram.org/bot{CONFIG['telegram_token']}/sendMessage"
        requests.post(url, json={"chat_id": CONFIG["telegram_chat_id"], "text": msg}, timeout=5)
    except Exception:
        pass

def log(msg: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {msg}"
    print(line)
    with open(CONFIG["log_file"], "a") as f:
        f.write(line + "\n")

# ==================== INDICATORS ====================
def sma(series: pd.Series, period: int) -> pd.Series:
    return series.rolling(period).mean()

def rsi(series: pd.Series, period: int = 14) -> pd.Series:
    delta = series.diff()
    gain = delta.where(delta > 0, 0).rolling(period).mean()
    loss = -delta.where(delta < 0, 0).rolling(period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def macd(series: pd.Series, fast=12, slow=26, signal=9):
    ema_fast = series.ewm(span=fast).mean()
    ema_slow = series.ewm(span=slow).mean()
    macd_line = ema_fast - ema_slow
    signal_line = macd_line.ewm(span=signal).mean()
    hist = macd_line - signal_line
    return macd_line, signal_line, hist

# ==================== STRATEGY ====================
def analyze(df: pd.DataFrame) -> dict:
    """
    Return signal: {'side': 'buy'|'sell'|None, 'reason': str, 'sl': float, 'tp': float}
    Modified to respect bias from plumbing verdict.
    """
    close = df['close']
    high = df['high']
    low = df['low']
    vol = df['tick_volume']

    # Indicators
    df['sma20'] = sma(close, 20)
    df['sma50'] = sma(close, 50)
    df['sma200'] = sma(close, 200)
    df['rsi'] = rsi(close, 14)
    macd_line, signal_line, hist = macd(close)
    df['macd'] = macd_line
    df['macd_signal'] = signal_line
    df['macd_hist'] = hist
    df['vol_avg20'] = sma(vol, 20)

    last = df.iloc[-1]
    prev = df.iloc[-2]

    price = last['close']
    atr = (high - low).rolling(14).mean().iloc[-1]

    vol_ok = last['tick_volume'] > last['vol_avg20'] * 1.2

    # ==== BIAS FILTER FROM PLUMBING VERDICT ====
    bias = CONFIG.get("bias", "NEUTRAL")
    trade_mode = CONFIG.get("trade_mode", "NORMAL")
    
    # FLAT mode = no trades
    if trade_mode == "FLAT":
        return {"side": None, "reason": "Trade mode FLAT — no trades per plumbing verdict", "sl": 0, "tp": 0}

    # ==== SETUP RULES (modified for bias) ====
    # Long: RSI < 45 + price > SMA20 + MACD histogram turning up + vol > avg
    # Short: RSI > 55 + price < SMA20 + MACD histogram turning down + vol > avg

    # LONG SETUP
    long_setup = (
        last['rsi'] < 45 and
        price > last['sma20'] and
        last['macd_hist'] > prev['macd_hist'] and
        last['macd_hist'] > 0 and
        vol_ok
    )

    # SHORT SETUP
    short_setup = (
        last['rsi'] > 55 and
        price < last['sma20'] and
        last['macd_hist'] < prev['macd_hist'] and
        last['macd_hist'] < 0 and
        vol_ok
    )

    # Apply bias filter
    if bias == "BULLISH" and not long_setup:
        return {"side": None, "reason": "Bullish bias but no long setup", "sl": 0, "tp": 0}
    if bias == "BEARISH" and not short_setup:
        return {"side": None, "reason": "Bearish bias but no short setup", "sl": 0, "tp": 0}
    if bias == "NEUTRAL" and not (long_setup or short_setup):
        return {"side": None, "reason": "No setup (neutral bias)", "sl": 0, "tp": 0}

    # Determine side
    if long_setup and (bias in ["BULLISH", "NEUTRAL"]):
        sl = price - atr * 1.5
        tp = price + atr * 3.0
        return {"side": "buy", "reason": "RSI oversold + trend + MACD flip + vol (bullish/neutral bias)", "sl": sl, "tp": tp}

    if short_setup and (bias in ["BEARISH", "NEUTRAL"]):
        sl = price + atr * 1.5
        tp = price - atr * 3.0
        return {"side": "sell", "reason": "RSI overbought + trend + MACD flip + vol (bearish/neutral bias)", "sl": sl, "tp": tp}

    return {"side": None, "reason": "Setup conflicts with bias", "sl": 0, "tp": 0}


# ==================== POSITION MANAGEMENT ====================
def get_open_positions(symbol: str):
    positions = mt5.positions_get(symbol=symbol)
    return positions if positions else ()

def has_open_position(symbol: str, side: str) -> bool:
    for pos in get_open_positions(symbol):
        if (side == "buy" and pos.type == mt5.ORDER_TYPE_BUY) or \
           (side == "sell" and pos.type == mt5.ORDER_TYPE_SELL):
            return True
    return False

def count_open_positions(symbol: str) -> int:
    positions = get_open_positions(symbol)
    return len(positions)


# ==================== ORDER EXECUTION ====================
def place_order(symbol: str, side: str, volume: float, sl: float, tp: float) -> bool:
    if CONFIG["dry_run"]:
        log(f"[DRY RUN] {side.upper()} {volume} {symbol} @ market | SL: {sl:.2f} TP: {tp:.2f}")
        send_telegram(f"📝 DRY RUN: {side.upper()} {volume} {symbol} SL:{sl:.0f} TP:{tp:.0f}")
        return True

    tick = mt5.symbol_info_tick(symbol)
    if not tick:
        log(f"❌ No tick for {symbol}")
        return False

    price = tick.ask if side == "buy" else tick.bid
    order_type = mt5.ORDER_TYPE_BUY if side == "buy" else mt5.ORDER_TYPE_SELL

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": volume,
        "type": order_type,
        "price": price,
        "sl": sl,
        "tp": tp,
        "deviation": 20,
        "magic": CONFIG["magic_number"],
        "comment": CONFIG["comment"],
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }

    result = mt5.order_send(request)
    if result.retcode == mt5.TRADE_RETCODE_DONE:
        log(f"✅ ORDER FILLED: {side.upper()} {volume} {symbol} @ {price:.2f} | SL:{sl:.2f} TP:{tp:.2f} | Ticket:{result.order}")
        send_telegram(f"✅ FILLED: {side.upper()} {volume} {symbol} @ {price:.0f} SL:{sl:.0f} TP:{tp:.0f}")
        return True
    else:
        log(f"❌ ORDER FAILED: {result.retcode} - {result.comment}")
        send_telegram(f"❌ FAILED: {side.upper()} {symbol} - {result.comment}")
        return False


def calc_volume(symbol: str, sl_price: float) -> float:
    """Risk-based position sizing with max_contracts cap"""
    info = mt5.account_info()
    if not info:
        return 0.01
    equity = info.equity
    risk_amount = equity * (CONFIG["risk_pct"] / 100)

    sym_info = mt5.symbol_info(symbol)
    if not sym_info:
        return 0.01

    tick_value = sym_info.trade_tick_value
    tick_size = sym_info.trade_tick_size
    point = sym_info.point

    current_price = sym_info.bid if CONFIG["dry_run"] else mt5.symbol_info_tick(symbol).bid
    sl_distance_points = abs(current_price - sl_price) / point

    if sl_distance_points == 0:
        return 0.01

    volume = risk_amount / (sl_distance_points * tick_value)
    volume = max(sym_info.volume_min, min(sym_info.volume_max, round(volume / sym_info.volume_step) * sym_info.volume_step))
    
    # Cap at max_contracts from orchestrator
    max_contracts = CONFIG.get("max_contracts", 1)
    if volume > max_contracts:
        volume = max_contracts
        log(f"⚠️ Volume capped at max_contracts={max_contracts}")
    
    return volume


# ==================== MAIN LOOP ====================
def run_bot():
    log("=" * 50)
    log(f"🚀 Starting MT5 Bot | Symbol: {CONFIG['symbol']} | Mode: {CONFIG['trade_mode']} | Bias: {CONFIG['bias']} | Max Contracts: {CONFIG['max_contracts']} | Dry-run: {CONFIG['dry_run']}")
    send_telegram(f"🚀 Bot started | {CONFIG['symbol']} | {CONFIG['trade_mode']} | {CONFIG['bias']} | Dry-run: {CONFIG['dry_run']}")

    # Initialize MT5
    if not mt5.initialize():
        log(f"❌ MT5 init failed: {mt5.last_error()}")
        return

    log("✅ MT5 initialized")

    # Select symbol
    if not mt5.symbol_select(CONFIG["symbol"], True):
        log(f"❌ Symbol select failed: {mt5.last_error()}")
        mt5.shutdown()
        return

    log(f"✅ Symbol {CONFIG['symbol']} selected")

    # Timeframe mapping
    tf_map = {
        "M1": mt5.TIMEFRAME_M1,
        "M5": mt5.TIMEFRAME_M5,
        "M15": mt5.TIMEFRAME_M15,
        "H1": mt5.TIMEFRAME_H1,
        "H4": mt5.TIMEFRAME_H4,
        "D1": mt5.TIMEFRAME_D1,
    }
    timeframe = tf_map.get(CONFIG["timeframe"], mt5.TIMEFRAME_H1)

    try:
        while True:
            # Check if we should still trade (execution window 06:30-09:00 PT)
            now = datetime.now()
            current_time = now.time()
            if current_time < time(6, 30) or current_time > time(9, 0):
                log(f"⏰ Outside execution window (06:30-09:00 PT). Current: {current_time}. Sleeping 60s...")
                tm.sleep(60)
                continue

            # Check daily trade limit (max 2 trades per session per multi-account-gateway.md)
            open_pos_count = count_open_positions(CONFIG["symbol"])
            if open_pos_count >= 2:
                log(f"⚠️ Max 2 positions reached. Waiting for closure...")
                tm.sleep(300)
                continue

            # Get data
            rates = mt5.copy_rates_from_pos(CONFIG["symbol"], timeframe, 0, CONFIG["lookback_bars"])
            if rates is None or len(rates) < 100:
                log("⚠️ Not enough data, waiting...")
                tm.sleep(60)
                continue

            df = pd.DataFrame(rates)
            df['time'] = pd.to_datetime(df['time'], unit='s')
            df.set_index('time', inplace=True)

            # Analyze
            signal = analyze(df)
            log(f"📊 Signal: {signal['side'] or 'NONE'} | {signal['reason']} | RSI: {df['rsi'].iloc[-1]:.1f} | MACDh: {df['macd_hist'].iloc[-1]:.0f}")

            # Execute if setup
            if signal['side'] and not has_open_position(CONFIG["symbol"], signal['side']):
                vol = calc_volume(CONFIG["symbol"], signal['sl'])
                if vol > 0:
                    log(f"🎯 Setup detected: {signal['side'].upper()} | Vol: {vol} | SL: {signal['sl']:.2f} | TP: {signal['tp']:.2f}")
                    place_order(CONFIG["symbol"], signal['side'], vol, signal['sl'], signal['tp'])
                else:
                    log("⚠️ Volume calc failed")

            # Sleep to next candle
            next_candle = (now.replace(minute=0, second=0, microsecond=0) + pd.Timedelta(hours=1))
            sleep_sec = (next_candle - now).total_seconds() + 5
            log(f"😴 Sleeping {sleep_sec:.0f}s until next candle...")
            tm.sleep(sleep_sec)

    except KeyboardInterrupt:
        log("🛑 Stopped by user")
    except Exception as e:
        log(f"💥 ERROR: {e}")
        send_telegram(f"💥 Bot error: {e}")
    finally:
        mt5.shutdown()
        log("🔌 MT5 shutdown complete")


if __name__ == "__main__":
    run_bot()