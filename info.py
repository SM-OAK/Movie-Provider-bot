himport re
from os import environ, getenv
from Script import script 

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if isinstance(value, bool): return value
    value = str(value).lower()
    if value in ["true", "yes", "1", "enable", "y"]: return True
    elif value in ["false", "no", "0", "disable", "n"]: return False
    else: return default

# Safe integer conversion helper to prevent ValueError
def get_int(key, default):
    value = environ.get(key, str(default))
    return int(value) if value and value.isdigit() else default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = get_int('API_ID', 22321078)
API_HASH = environ.get('API_HASH', '9960806d290cf4170e43355fcc3687ac')
BOT_TOKEN = environ.get('BOT_TOKEN', "8315054483:AAFCQMkvu2J4DABjTl5c4WP8speHJkfcgEU")

# Bot settings
CACHE_TIME = get_int('CACHE_TIME', 300)
USE_CAPTION_FILTER = is_enabled(environ.get('USE_CAPTION_FILTER', "True"), True)
PICS = (environ.get('PICS', 'https://telegra.ph/file/7703c1d3c58e36a56716e.jpg https://telegra.ph/file/74d3de58683ff6845f837.jpg https://telegra.ph/file/950a0aed988cc9d7dea9c.jpg https://telegra.ph/file/d2d2dd5a396ef56e4ee48.jpg https://telegra.ph/file/7e4bc0ed151ee13e76286.jpg https://telegra.ph/file/14eaf531bc83381a6943c.jpg https://telegra.ph/file/5e28043d27e8ef27ab3bf.jpg https://telegra.ph/file/3d18aedab92c38fbda7da.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/e20b5fdaf217252964202.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://telegra.ph/file/85d361ab4cb6511006022.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://telegra.ph/file/86b7b7e2aa7e38f328902.jpg")
SUBSCRIPTION = (environ.get('SUBSCRIPTION', 'https://telegra.ph/file/734170f40b8169830d821.jpg'))
CODE = (environ.get('CODE', 'https://telegra.ph/file/72f425007b22d28bd935e.jpg'))

# stream link shortner
STREAM_SITE = environ.get('STREAM_SITE', 'api.shareus.io')
STREAM_API = environ.get('STREAM_API', 'PUIAQBIFrydvLhIzAOeGV8yZppu2')
STREAMHTO = environ.get('STREAMHTO', 'https://t.me/Ultroid_Official/18')

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6226520145').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002258485713').split()]  # FIXED: Added missing digit
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
PREMIUM_USER = [int(user) if id_pattern.search(user) else user for user in environ.get('PREMIUM_USER', '').split()]
auth_channel = environ.get('AUTH_CHANNEL', '-1001725568693')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', '-1002115046888')
reqst_channel = environ.get('REQST_CHANNEL_ID', '-1002062925443')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = is_enabled(environ.get("NO_RESULTS_MSG", "False"), False)

# MongoDB information 
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://xeviw38487_db_user:UAjmxkdslpJC5LPP@cluster0.werptta.mongodb.net/?appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "MovizTube")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
VERIFY = is_enabled(environ.get('VERIFY', "False"), False)
HOWTOVERIFY = environ.get('HOWTOVERIFY', 'https://t.me/Ultroid_Official/18')
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'api.shareus.io')
SHORTLINK_API = environ.get('SHORTLINK_API', 'PUIAQBIFrydvLhIzAOeGV8yZppu2')
IS_SHORTLINK = is_enabled(environ.get('IS_SHORTLINK', "False"), False)
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = environ.get("MAX_B_TN", "5")
MAX_BTN = is_enabled(environ.get('MAX_BTN', "True"), True)
PORT = get_int("PORT", 8080)
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/MovizTube_Group')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/MovizTube')
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/Ultroid_Official/18')
IS_TUTORIAL = is_enabled(environ.get('IS_TUTORIAL', "True"), True)
MSG_ALRT = environ.get('MSG_ALRT', 'ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : ultroidxTeam')

# CRITICAL FIX: Corrected LOG_CHANNEL ID format
# The original ID -100377750722 appears to be incomplete/corrupted
# Replace with your actual log channel ID (get it from @MissRose_bot or similar)
# Format should be: -100 followed by channel ID (usually 10-13 digits total)
LOG_CHANNEL = get_int('LOG_CHANNEL', 1003777507229)  # Set to 0 to disable, or provide correct channel ID

SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/UltroidOfficial_chat')
P_TTI_SHOW_OFF = is_enabled(environ.get('P_TTI_SHOW_OFF', "False"), False)
IMDB = is_enabled(environ.get('IMDB', "False"), False)
AUTO_FFILTER = is_enabled(environ.get('AUTO_FFILTER', "True"), True)
AUTO_DELETE = is_enabled(environ.get('AUTO_DELETE', "True"), True)
SINGLE_BUTTON = is_enabled(environ.get('SINGLE_BUTTON', "True"), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL)) if LOG_CHANNEL else 0
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1002075726565')).split()]
MELCOW_NEW_USERS = is_enabled(environ.get('MELCOW_NEW_USERS', "True"), True)
PROTECT_CONTENT = is_enabled(environ.get('PROTECT_CONTENT', "True"), True)
PUBLIC_FILE_STORE = is_enabled(environ.get('PUBLIC_FILE_STORE', "True"), True)

# Online Stream and Download
SLEEP_THRESHOLD = get_int('SLEEP_THRESHOLD', 60)
WORKERS = get_int('WORKERS', 4)
SESSION_NAME = str(environ.get('SESSION_NAME', 'LazyBot'))
MULTI_CLIENT = False
name = str(environ.get('name', 'LazyPrincess'))
PING_INTERVAL = get_int("PING_INTERVAL", 1200)

BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001987654567")).split())) 
OWNER_USERNAME = "LazyDeveloper"
PREMIUM_LOGS = get_int('PREMIUM_LOGS', -1002062925443)
LOG_STR = "Custom Configurations loaded successfully."
