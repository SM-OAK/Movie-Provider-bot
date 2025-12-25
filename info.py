import re
from os import environ, getenv
from Script import script 

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# ==========================================
# Bot Information (Taken from your VJ Configs)
# ==========================================
SESSION = environ.get('SESSION', 'YeshVJBot')
API_ID = int(environ.get('API_ID', '22321078'))
API_HASH = environ.get('API_HASH', '9960806d290cf4170e43355fcc3687ac')
BOT_TOKEN = environ.get('BOT_TOKEN', "8200587392:AAGOoy6_fjH3BkI4jfYH6XbSJdbNyc8qfHQ")

# ==========================================
# Bot Settings & Visuals
# ==========================================
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://i.ibb.co/qpxpGmC/image.jpg https://i.ibb.co/DQ35zLZ/image.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/e20b5fdaf217252964202.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://telegra.ph/file/85d361ab4cb6511006022.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://telegra.ph/file/86b7b7e2aa7e38f328902.jpg")

# ==========================================
# Admins, Channels & Users
# ==========================================
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6226520145 7219461396').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1003303429005').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '7219461396').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []

# Force Subscribe & Logs
AUTH_CHANNEL = int(environ.get('AUTH_CHANNEL', '')) # Defaulted from your search config
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002062925443'))
REQST_CHANNEL = int(environ.get('REQST_CHANNEL_ID', '-1002062925443'))
SUPPORT_CHAT_ID = int(environ.get('SUPPORT_CHAT_ID', '-1002115046888'))

# ==========================================
# MongoDB Information
# ==========================================
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://xeviw38487_db_user:UAjmxkdslpJC5LPP@cluster0.werptta.mongodb.net/?appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# ==========================================
# Shortener & Verification
# ==========================================
VERIFY = bool(environ.get('VERIFY', False))
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'api.shareus.io')
SHORTLINK_API = environ.get('SHORTLINK_API', 'PUIAQBIFrydvLhIzAOeGV8yZppu2')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', False))
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/Ultroid_Official/18')

# ==========================================
# Links & Alerts
# ==========================================
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/+rC0W_RoQBCc1MGY1')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/vj_bots')
MSG_ALRT = environ.get('MSG_ALRT', 'Hello My Dear Friends ❤️')
OWNER_USERNAME = "SM_OAK" # Updated based on your link

# ==========================================
# Feature Toggles
# ==========================================
IMDB = is_enabled((environ.get('IMDB', "False")), False)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), True)

# ==========================================
# Server & Hosting Logic
# ==========================================
PORT = int(environ.get('PORT', 8080))
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = environ.get('APP_NAME')
else:
    ON_HEROKU = False

BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
HAS_SSL = bool(getenv('HAS_SSL', False))

if HAS_SSL:
    URL = "https://{}/".format(FQDN)
else:
    URL = "http://{}/".format(FQDN)

# ==========================================
# Scripts & Templates
# ==========================================
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)

# Lists
LANGUAGES = ["malayalam", "tamil", "english", "hindi", "telugu", "kannada", "gujarati", "marathi", "punjabi"]
QUALITIES = ["360P", "480P", "720P", "1080P", "1440P", "2160P"]
BUTTON_MODE = bool(environ.get('BUTTON_MODE', True))
MAX_BTN = bool(environ.get('MAX_BTN', True))
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', True))
IMDB = bool(environ.get('IMDB', False))
AUTO_FFILTER = bool(environ.get('AUTO_FFILTER', True))
AUTO_DELETE = bool(environ.get('AUTO_DELETE', True))
LONG_IMDB_DESCRIPTION = bool(environ.get("LONG_IMDB_DESCRIPTION", False))
SPELL_CHECK_REPLY = bool(environ.get("SPELL_CHECK_REPLY", True))
MELCOW_NEW_USERS = bool(environ.get('MELCOW_NEW_USERS', True))
PROTECT_CONTENT = bool(environ.get('PROTECT_CONTENT', True))
PUBLIC_FILE_STORE = bool(environ.get('PUBLIC_FILE_STORE', True))
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", False))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))


# Token Verification Info :
VERIFY = bool(environ.get('VERIFY', False))
VERIFY_SHORTLINK_URL = environ.get('VERIFY_SHORTLINK_URL', 'api.shareus.io')
VERIFY_SHORTLINK_API = environ.get('VERIFY_SHORTLINK_API', 'PUIAQBIFrydvLhIzAOeGV8yZppu2')
VERIFY_TUTORIAL = environ.get('VERIFY_TUTORIAL', 'https://t.me/Ultroid_Official/18')

# Shortlink Info
SHORTLINK_MODE = bool(environ.get('SHORTLINK_MODE', False)) 
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'api.shareus.io')
SHORTLINK_API = environ.get('SHORTLINK_API', 'PUIAQBIFrydvLhIzAOeGV8yZppu2')
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/Ultroid_Official/18') 


# Others
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
MAX_B_TN = environ.get("MAX_B_TN", "5")
PORT = environ.get("PORT", "8080")
MSG_ALRT = environ.get('MSG_ALRT', 'ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : ultroidxTeam')
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)


# Choose Option Settings 
LANGUAGES = ["malayalam", "tamil", "english", "hindi", "telugu", "kannada", "gujarati", "marathi", "punjabi"]
SEASONS = ["season 1", "season 2", "season 3", "season 4", "season 5", "season 6", "season 7", "season 8", "season 9", "season 10"]
QUALITIES = ["360p", "480p", "720p", "1080p", "1440p", "2160p"]
YEARS = ["2020", "2021", "2022", "2023", "2024", "2025"]


# Online Stream and Download
STREAM_MODE = bool(environ.get('STREAM_MODE', True)) 
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "")


# Rename Info
RENAME_MODE = bool(environ.get('RENAME_MODE', False)) 
AUTO_APPROVE_MODE = bool(environ.get('AUTO_APPROVE_MODE', False)) 


# Start Command Reactions
REACTIONS = ["🤝", "😇", "🤗", "😍", "👍", "🎅", "🔥", "⚡️", "🫡", "😎", "🤩"] 


if MULTIPLE_DATABASE == False:
    USER_DB_URI = DATABASE_URI
    OTHER_DB_URI = DATABASE_URI
    FILE_DB_URI = DATABASE_URI
    SEC_FILE_DB_URI = DATABASE_URI
else:
    USER_DB_URI = DATABASE_URI    
    OTHER_DB_URI = O_DB_URI       
    FILE_DB_URI = F_DB_URI        
    SEC_FILE_DB_URI = S_DB_URI    

# Don't Remove Credit @VJ_Bots
