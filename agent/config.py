"""
config.py — Central config for the Hinglish Recovery Agent
──────────────────────────────────────────────────────────
Set your keys here OR use environment variables.
Never commit real keys to git.
"""

import os
from pathlib import Path

# Auto-load .env from project root (parent of agent/)
try:
    from dotenv import load_dotenv
    _env_file = Path(__file__).parent.parent / ".env"
    if _env_file.exists():
        load_dotenv(_env_file)
except ImportError:
    pass  # dotenv optional — fall back to system env vars

# ── API Keys ────────────────────────────────────────────────────────────
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "YOUR_CLAUDE_API_KEY_HERE")
RAZORPAY_KEY_ID   = os.environ.get("RAZORPAY_KEY_ID",   "YOUR_RAZORPAY_TEST_KEY_ID")
RAZORPAY_KEY_SECRET = os.environ.get("RAZORPAY_KEY_SECRET", "YOUR_RAZORPAY_TEST_SECRET")

# ── Claude model ─────────────────────────────────────────────────────────
CLAUDE_MODEL = "claude-sonnet-4-5"   # fast + smart; swap to opus for higher quality

# ── Paths ────────────────────────────────────────────────────────────────
ROOT_DIR     = Path(__file__).parent.parent
DATA_DIR     = ROOT_DIR / "data"
LOGS_DIR     = ROOT_DIR / "logs"
RECORDS_FILE = DATA_DIR / "synthetic_records.json"
AUDIT_DB     = LOGS_DIR / "audit_log.json"
PROMISES_DB  = LOGS_DIR / "promise_tracker.json"

# ── Agent bounding rules ─────────────────────────────────────────────────
HIGH_VALUE_GATE_INR  = 10_000   # ₹ threshold — must log gate check
HUMAN_REVIEW_INR     = 50_000   # ₹ threshold — escalate to human, no auto-retry
MAX_PROMISES_BROKEN  = 2        # after this many broken promises → STOP
OUTREACH_COOLDOWN_HRS = 24      # min hours between messages to same customer
