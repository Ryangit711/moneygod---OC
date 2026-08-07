#!/usr/bin/env python3
"""
ROBUST PILOT RUNNER
Runs the complete trading pipeline with error handling, logging, and state management.
Designed to run unattended via cron or systemd.
"""

import sys
import json
import logging
import traceback
from datetime import datetime, timezone
from pathlib import Path

# Add trading_system to path
sys.path.insert(0, str(Path(__file__).parent))

from orchestrator import TradingOrchestrator


# ==================== LOGGING SETUP ====================

LOG_DIR = Path(__file__).parent / "logs"
LOG_DIR.mkdir(exist_ok=True)

log_file = LOG_DIR / f"pilot_{datetime.now().strftime('%Y%m%d')}.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(message)s",
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(sys.stdout),
    ],
)
logger = logging.getLogger(__name__)


# ==================== STATE MANAGEMENT ====================

STATE_FILE = Path(__file__).parent / "pilot_state.json"


def load_state() -> dict:
    """Load persistent state (last run, consecutive failures, etc.)"""
    if STATE_FILE.exists():
        try:
            with open(STATE_FILE) as f:
                return json.load(f)
        except Exception:
            pass
    return {
        "last_successful_run": None,
        "consecutive_failures": 0,
        "total_runs": 0,
        "total_successes": 0,
    }


def save_state(state: dict):
    """Save persistent state."""
    try:
        with open(STATE_FILE, "w") as f:
            json.dump(state, f, indent=2)
    except Exception as e:
        logger.error(f"Failed to save state: {e}")


# ==================== MAIN PILOT LOOP ====================

def run_pilot(config_path: str = "config.json", max_retries: int = 3) -> bool:
    """
    Run the complete trading pipeline with retries and error handling.
    Returns True if successful, False otherwise.
    """
    state = load_state()
    state["total_runs"] += 1
    
    logger.info("=" * 60)
    logger.info("🚀 PILOT RUN STARTED")
    logger.info("=" * 60)
    logger.info(f"Run #{state['total_runs']} | Failures: {state['consecutive_failures']}")
    
    for attempt in range(1, max_retries + 1):
        try:
            logger.info(f"Attempt {attempt}/{max_retries}")
            
            # Initialize orchestrator
            orchestrator = TradingOrchestrator(config_path)
            
            # Run full pipeline
            orchestrator.run_full_pipeline()
            
            # Success!
            state["last_successful_run"] = datetime.now(timezone.utc).isoformat()
            state["consecutive_failures"] = 0
            state["total_successes"] += 1
            save_state(state)
            
            logger.info("✅ PILOT RUN COMPLETED SUCCESSFULLY")
            return True
            
        except KeyboardInterrupt:
            logger.warning("⚠️ Interrupted by user")
            raise
            
        except Exception as e:
            logger.error(f"❌ Attempt {attempt} failed: {e}")
            logger.error(traceback.format_exc())
            
            if attempt < max_retries:
                import time
                wait_time = 60 * attempt  # 60s, 120s, 180s...
                logger.info(f"Retrying in {wait_time}s...")
                time.sleep(wait_time)
            else:
                logger.error("All retries exhausted")
    
    # All retries failed
    state["consecutive_failures"] += 1
    save_state(state)
    
    # Alert if too many consecutive failures
    if state["consecutive_failures"] >= 3:
        logger.critical("🚨 3+ CONSECUTIVE FAILURES - MANUAL INTERVENTION NEEDED")
        # Could send Telegram alert here
    
    return False


def run_quick_check(config_path: str = "config.json") -> dict:
    """Run just the plumbing check (for cron every 30 min during market hours)."""
    logger.info("Running quick plumbing check...")
    
    try:
        orchestrator = TradingOrchestrator(config_path)
        verdict = orchestrator.run_plumbing_check()
        
        return {
            "success": True,
            "trade_mode": verdict.trade_mode,
            "bias": verdict.bias,
            "instrument": verdict.instrument,
            "net_liquidity": verdict.liquidity.net_liquidity_b,
        }
    except Exception as e:
        logger.error(f"Quick check failed: {e}")
        logger.error(traceback.format_exc())
        return {"success": False, "error": str(e)}


# ==================== ENTRY POINTS ====================

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Trading System Pilot Runner")
    parser.add_argument("--mode", choices=["full", "quick", "background"], default="full",
                        help="Run full pipeline, quick plumbing check, or background (alias for full)")
    parser.add_argument("--config", default="config.json", help="Config file path")
    parser.add_argument("--retries", type=int, default=3, help="Max retries for full run")
    
    args = parser.parse_args()
    
    if args.mode in ("full", "background"):
        success = run_pilot(args.config, args.retries)
        sys.exit(0 if success else 1)
    else:
        result = run_quick_check(args.config)
        print(json.dumps(result, indent=2))
        sys.exit(0 if result["success"] else 1)