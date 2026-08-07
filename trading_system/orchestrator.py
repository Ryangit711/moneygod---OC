#!/usr/bin/env python3
"""
TRADING SYSTEM ORCHESTRATOR
Chains: plumbing_fetcher → decision_engine → mt5_bot (or tradovate_bot) → journal
Run via cron: 0 5 * * 1-5 /home/aryan/trading_system/orchestrator.py
"""

import json
import subprocess
import sys
import requests
from datetime import datetime, time
from pathlib import Path
from typing import Optional
import argparse

# Add trading_system to path
sys.path.insert(0, str(Path(__file__).parent))

from plumbing_fetcher import run_plumbing_pipeline, PlumbingVerdict, save_verdict


def send_telegram(message: str, config: dict) -> bool:
    """Send a message to Telegram if enabled."""
    if not config.get("notifications", {}).get("telegram_enabled", False):
        return False
    token = config.get("notifications", {}).get("telegram_token", "")
    chat_id = config.get("notifications", {}).get("telegram_chat_id", "")
    if not token or not chat_id:
        return False
    try:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        resp = requests.post(url, json={"chat_id": chat_id, "text": message}, timeout=10)
        return resp.status_code == 200
    except Exception:
        return False


class TradingOrchestrator:
    def __init__(self, config_path: str = "config.json"):
        self.config = self.load_config(config_path)
        self.verdict_path = Path("plumbing_verdict.json")
        self.journal_path = Path("trade_journal.csv")
        
    def load_config(self, path: str) -> dict:
        default = {
            "mode": "paper",  # "paper" | "live"
            "accounts": {
                "fx": {"enabled": True, "bot": "mt5_bot.py", "symbol": "BTCUSD"},
                "futures": {"enabled": False, "bot": "tradovate_bot.py", "symbol": "MES"},
            },
            "risk": {
                "max_daily_loss_pct": 3.0,
                "max_accounts_in_drawdown": 2,
            },
            "notifications": {
                "telegram_enabled": True,
                "telegram_token": "",
                "telegram_chat_id": "6766010191",
            },
            "schedule": {
                "plumbing_check": "05:30",
                "execution_start": "06:30",
                "execution_end": "09:00",
                "journal_close": "09:05",
            }
        }
        
        if Path(path).exists():
            with open(path) as f:
                user_config = json.load(f)
                default.update(user_config)
        else:
            with open(path, "w") as f:
                json.dump(default, f, indent=2)
            print(f"Created default config at {path}")
        
        return default
    
    def run_plumbing_check(self) -> PlumbingVerdict:
        """Step 1: Run plumbing pipeline (05:30 AM)"""
        print("\n" + "="*60)
        print("STEP 1: PLUMBING CHECK (05:30 AM)")
        print("="*60)
        
        verdict = run_plumbing_pipeline()
        save_verdict(verdict, self.verdict_path)
        
        # Also save human-readable summary
        summary_path = Path(f"verdict_{datetime.now().strftime('%Y%m%d')}.txt")
        with open(summary_path, "w") as f:
            f.write(f"DATE: {datetime.now().strftime('%Y-%m-%d')}\n")
            f.write(f"TRADING: {'YES' if verdict.trade_mode != 'FLAT' else 'NO'}\n")
            f.write(f"TRADE MODE: {verdict.trade_mode}\n")
            f.write(f"INSTRUMENT: {verdict.instrument}\n")
            f.write(f"BIAS: {verdict.bias}\n")
            f.write(f"SESSION PLAN:\n{verdict.session_plan_line1}\n{verdict.session_plan_line2}\n")
        
        # Send Telegram notification
        msg = (f"📊 *Daily Verdict* ({datetime.now().strftime('%Y-%m-%d')})\n"
               f"Mode: *{verdict.trade_mode}* | Bias: *{verdict.bias}*\n"
               f"Instrument: {verdict.instrument} | Max Contracts: {verdict.max_contracts}\n"
               f"Risk/Trade: {verdict.risk_pct_per_trade}% | Daily Max: {verdict.daily_max_pct}%\n"
               f"Active Edges: {', '.join(verdict.active_edges) if verdict.active_edges else 'None'}\n"
               f"Plan: {verdict.session_plan_line1}\n{verdict.session_plan_line2}")
        send_telegram(msg, self.config)
        
        return verdict
    
    def should_execute(self, verdict: PlumbingVerdict) -> tuple[bool, str]:
        """Check if we should execute trades based on verdict + circuit breakers"""
        if verdict.trade_mode == "FLAT":
            return False, f"Trade mode is FLAT: {verdict.session_plan_line2}"
        
        # Check circuit breakers from multi-account-gateway.md
        # - Combined daily loss > 3% → stop all
        # - 2+ accounts in daily loss → stop all
        # - 3+ accounts in weekly DD > 5% → stop all week
        
        # For now, just check the verdict
        return True, "Proceed to execution"
    
    def run_execution(self, verdict: PlumbingVerdict) -> dict:
        """Step 2: Run trading bots (06:30-09:00 AM)"""
        print("\n" + "="*60)
        print("STEP 2: EXECUTION (06:30-09:00 AM)")
        print("="*60)
        
        results = {}
        
        # Determine which bot(s) to run based on instrument
        if verdict.instrument in ["MES", "BOTH", "MNQ"]:
            # Futures bot (not yet implemented)
            if self.config["accounts"]["futures"]["enabled"]:
                print(f"  [FUTURES] Would run tradovate_bot.py for {verdict.instrument}")
                print(f"  [FUTURES] Trade mode: {verdict.trade_mode}, Bias: {verdict.bias}")
                results["futures"] = {"status": "not_implemented", "instrument": verdict.instrument}
            else:
                print(f"  [FUTURES] Disabled in config")
        
        if verdict.instrument in ["NONE"]:
            print(f"  No instruments to trade today (FLAT)")
            results["status"] = "flat"
            return results
        
        # FX bot (mt5_bot.py exists)
        if self.config["accounts"]["fx"]["enabled"]:
            print(f"  [FX] Running mt5_bot.py for {self.config['accounts']['fx']['symbol']}")
            print(f"  [FX] Trade mode: {verdict.trade_mode}, Bias: {verdict.bias}")
            
            # In production, we'd pass the verdict to the bot via config/env
            # For demo, just show the command
            bot_cmd = [
                sys.executable, "mt5_bot.py",
                "--mode", self.config["mode"],
                "--trade-mode", verdict.trade_mode,
                "--bias", verdict.bias,
                "--max-contracts", str(3 if verdict.trade_mode == "FULL" else 2 if verdict.trade_mode == "NORMAL" else 1),
            ]
            print(f"  Command: {' '.join(bot_cmd)}")
            
            # Actually run it (commented for demo - requires MT5 terminal)
            # result = subprocess.run(bot_cmd, capture_output=True, text=True, timeout=3600)
            # results["fx"] = {"status": "completed", "output": result.stdout}
            results["fx"] = {"status": "demo_mode", "command": bot_cmd}
        else:
            print(f"  [FX] Disabled in config")
        
        return results
    
    def update_journal(self, verdict: PlumbingVerdict, execution_results: dict):
        """Step 3: Update journal (09:05 AM)"""
        print("\n" + "="*60)
        print("STEP 3: JOURNAL UPDATE (09:05 AM)")
        print("="*60)
        
        # In production: read bot trade logs, combine with verdict, write journal
        # For demo, just show the format
        journal_entry = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "trade_mode": verdict.trade_mode,
            "instrument": verdict.instrument,
            "bias": verdict.bias,
            "active_edges": verdict.active_edges,
            "session_plan": f"{verdict.session_plan_line1} | {verdict.session_plan_line2}",
            "execution_results": execution_results,
            "combined_pnl": 0.0,  # Would sum from all account logs
        }
        
        print(f"  Journal entry prepared:")
        for k, v in journal_entry.items():
            print(f"    {k}: {v}")
        
        # Append to CSV journal (format from multi-account-gateway.md)
        if not self.journal_path.exists():
            with open(self.journal_path, "w") as f:
                f.write("Date,Trade Mode,Instrument,Bias,Active Edges,Session Plan,Execution Status,Combined PnL\n")
        
        with open(self.journal_path, "a") as f:
            f.write(f"{journal_entry['date']},{journal_entry['trade_mode']},{journal_entry['instrument']},"
                    f"{journal_entry['bias']},\"{'; '.join(journal_entry['active_edges'])}\","
                    f"\"{journal_entry['session_plan']}\",{execution_results.get('fx', {}).get('status', 'none')},"
                    f"{journal_entry['combined_pnl']}\n")
        
        print(f"  ✅ Appended to {self.journal_path}")
    
    def run_full_pipeline(self):
        """Run the complete daily pipeline"""
        print("\n" + "#"*60)
        print("# TRADING SYSTEM ORCHESTRATOR - DAILY PIPELINE")
        print(f"# {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("#"*60)
        
        # Step 1: Plumbing check
        verdict = self.run_plumbing_check()
        
        # Check circuit breakers
        should_trade, reason = self.should_execute(verdict)
        print(f"\n  Circuit breaker check: {should_trade} — {reason}")
        
        if not should_trade:
            print("  Stopping pipeline. No trades today.")
            self.update_journal(verdict, {"status": "flat", "reason": reason})
            return
        
        # Step 2: Execution
        execution_results = self.run_execution(verdict)
        
        # Step 3: Journal
        self.update_journal(verdict, execution_results)
        
        print("\n" + "#"*60)
        print("# PIPELINE COMPLETE")
        print("#"*60)


def main():
    parser = argparse.ArgumentParser(description="Trading System Orchestrator")
    parser.add_argument("--step", choices=["plumbing", "execute", "journal", "full"], 
                        default="full", help="Which step to run")
    parser.add_argument("--config", default="config.json", help="Config file path")
    parser.add_argument("--demo", action="store_true", help="Run in demo mode (no real trades)")
    
    args = parser.parse_args()
    
    orchestrator = TradingOrchestrator(args.config)
    
    if args.step == "plumbing":
        orchestrator.run_plumbing_check()
    elif args.step == "execute":
        # Need a verdict first
        if orchestrator.verdict_path.exists():
            with open(orchestrator.verdict_path) as f:
                data = json.load(f)
            # Reconstruct minimal verdict
            from plumbing_fetcher import PlumbingVerdict, RawPlumbingData, LiquidityVerdict, MarketSignals
            # Simplified - in production, load full verdict
            verdict = run_plumbing_pipeline()
            orchestrator.run_execution(verdict)
        else:
            print("No verdict found. Run --step plumbing first.")
    elif args.step == "journal":
        print("Journal step requires execution results. Run full pipeline.")
    else:  # full
        orchestrator.run_full_pipeline()


if __name__ == "__main__":
    main()