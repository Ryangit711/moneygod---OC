#!/usr/bin/env bash
# ============================================================
# TRADING SYSTEM CRON SETUP
# Run this once to install the daily cron jobs
# ============================================================

set -e

TRADING_DIR="/home/aryan/trading_system"
PYTHON="/usr/bin/python3"

echo "Setting up trading system cron jobs..."

# Create cron entries
CRON_ENTRIES="
# Trading System - Daily Pipeline (Mon-Fri)
# 05:30 AM - Plumbing check
30 5 * * 1-5 cd $TRADING_DIR && $PYTHON orchestrator.py --step plumbing >> logs/plumbing_\$(date +\\%Y\\%m\\%d).log 2>&1

# 06:30 AM - Execution (runs continuously until 09:00)
30 6 * * 1-5 cd $TRADING_DIR && $PYTHON orchestrator.py --step execute >> logs/execute_\$(date +\\%Y\\%m\\%d).log 2>&1

# 09:05 AM - Journal close
5 9 * * 1-5 cd $TRADING_DIR && $PYTHON orchestrator.py --step journal >> logs/journal_\$(date +\\%Y\\%m\\%d).log 2>&1

# Weekly deep dive (Monday 04:30 AM - before plumbing check)
30 4 * * 1 cd $TRADING_DIR && $PYTHON weekly_deep_dive.py >> logs/weekly_\$(date +\\%Y\\%m\\%d).log 2>&1
"

# Create logs directory
mkdir -p "$TRADING_DIR/logs"

# Install cron (append to existing crontab)
(crontab -l 2>/dev/null | grep -v "trading_system"; echo "$CRON_ENTRIES") | crontab -

echo "✅ Cron jobs installed:"
crontab -l | grep -A 10 "Trading System"

echo ""
echo "To remove: crontab -l | grep -v trading_system | crontab -"
echo "To view logs: tail -f $TRADING_DIR/logs/*.log"