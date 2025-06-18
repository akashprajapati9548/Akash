# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⚙️ CONFIGURATION FILE
# 🔧 Designed by @WTF_NoHope & @Sanatani_Network
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

import os
import re
from dotenv import load_dotenv
from pyrogram import filters

# Load environment variables
load_dotenv()

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔐 Telegram Bot Credentials
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID", 0))
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "WTF_NoHope")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🗄️ Database & Hosting Config
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MONGO_DB_URI = os.getenv("MONGO_DB_URI")
LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", 0))
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔄 GitHub Updater
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

UPSTREAM_REPO = os.getenv("UPSTREAM_REPO", "https://github.com/akashprajapati9548/Akash")
UPSTREAM_BRANCH = os.getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = os.getenv("GIT_TOKEN")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔗 Support & Policy Links
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "https://t.me/Sanatani_Network")
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "https://t.me/AD_Creation_Chatzone")
PRIVACY_LINK = os.getenv("PRIVACY_LINK", "https://graph.org/Privacy-Policy-05-01-30")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⏱️ Duration & Playlist Settings
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DURATION_LIMIT_MIN = int(os.getenv("DURATION_LIMIT", 300))
PLAYLIST_FETCH_LIMIT = int(os.getenv("PLAYLIST_FETCH_LIMIT", 25))

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📦 File Size Limits (Bytes)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TG_AUDIO_FILESIZE_LIMIT = int(os.getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))       # 100MB
TG_VIDEO_FILESIZE_LIMIT = int(os.getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))      # 2GB

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🎵 Third-party Music API
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

API_KEY = os.getenv("API_KEY", "b9f6ba_IdlKyLphAbmvqqhVTJ-z1AIbNp5pMnMi")
API_URL = os.getenv("API_URL", "https://tgmusic.fallenapi.fun")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🎧 Spotify Credentials
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 💬 Session Strings (Pyrogram v2)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STRING1 = os.getenv("STRING_SESSION")
STRING2 = os.getenv("STRING_SESSION2")
STRING3 = os.getenv("STRING_SESSION3")
STRING4 = os.getenv("STRING_SESSION4")
STRING5 = os.getenv("STRING_SESSION5")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⚙️ Runtime Settings
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

AUTO_LEAVING_ASSISTANT = bool(os.getenv("AUTO_LEAVING_ASSISTANT", True))

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🖼️ Image URLs (Customizable)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DEFAULT_IMG = "https://files.catbox.moe/cky65b.jpg"

START_IMG_URL = os.getenv("START_IMG_URL", DEFAULT_IMG)
PING_IMG_URL = os.getenv("PING_IMG_URL", DEFAULT_IMG)
PLAYLIST_IMG_URL = DEFAULT_IMG
STATS_IMG_URL = DEFAULT_IMG
TELEGRAM_AUDIO_URL = DEFAULT_IMG
TELEGRAM_VIDEO_URL = DEFAULT_IMG
STREAM_IMG_URL = DEFAULT_IMG
SOUNDCLOUD_IMG_URL = DEFAULT_IMG
YOUTUBE_IMG_URL = DEFAULT_IMG
SPOTIFY_ARTIST_IMG_URL = DEFAULT_IMG
SPOTIFY_ALBUM_IMG_URL = DEFAULT_IMG
SPOTIFY_PLAYLIST_IMG_URL = DEFAULT_IMG

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔐 User & State Storage
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⏱️ Time Conversion
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def time_to_seconds(time: str) -> int:
    return sum(int(x) * 60**i for i, x in enumerate(reversed(time.split(":"))))

DURATION_LIMIT = time_to_seconds(f"{DURATION_LIMIT_MIN}:00")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ❌ Validate Support URLs
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

for name, url in {"SUPPORT_CHANNEL": SUPPORT_CHANNEL, "SUPPORT_GROUP": SUPPORT_GROUP}.items():
    if url and not re.match(r"^(?:http|https)://", url):
        raise SystemExit(f"[ERROR] - {name} URL is invalid. It must start with https://")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ✅ CONFIG LOADED SUCCESSFULLY
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
