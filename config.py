import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN", "")
DATABASE_URL = os.getenv("DATABASE_URL", "")

# Put Discord user IDs here, comma-separated.
ADMIN_USER_IDS = {
    int(x.strip()) for x in os.getenv("ADMIN_USER_IDS", "").split(",")
    if x.strip().isdigit()
}

# Crypto is intentionally disabled for this version.
# Deposit/withdraw UI remains available, but no real blockchain funds are moved.
LTC_XPUB = ""
LTC_DERIVATION_PATH = "m/84'/2'/0'/0"
MIN_WITHDRAW = 20

GAME_COOLDOWN_SECONDS = int(os.getenv("GAME_COOLDOWN_SECONDS", "2"))

# Existing bot code references these.
E = {
    "win": "✅",
    "loss": "❌",
    "points": "🪙",
}

# Demo display addresses only. They are not monitored and no funds are accepted.
DEMO_LTC_ADDRESS = os.getenv("DEMO_LTC_ADDRESS", "DEMO-LTC-ADDRESS")
DEMO_SOL_ADDRESS = os.getenv("DEMO_SOL_ADDRESS", "DEMO-SOL-ADDRESS")
