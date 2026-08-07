#!/usr/bin/env python3
"""
Cleanup old log files - keep only last 7 days
"""
import os
from pathlib import Path

logs = Path(__file__).parent / "logs"
for f in logs.glob("*.log"):
    if f.stat().st_mtime < (os.path.getmtime(logs) - 7 * 86400):
        f.unlink()
print("Cleaned old logs")