import sys
import glob
import importlib
from pathlib import Path
from pyrogram import idle
import logging
import logging.config

# Get logging configurations
try:
    logging.config.fileConfig('logging.conf')
except:
    # Fallback if logging.conf doesn't exist
    pass

logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("imdbpy").setLevel(logging.ERROR)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("aiohttp").setLevel(logging.ERROR)
logging.getLogger("aiohttp.web").setLevel(logging.ERROR)


from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from pyrogram.errors import PeerIdInvalid, ChannelInvalid, FloodWait
from database.ia_filterdb import Media
from database.users_chats_db import db
from info import *
from utils import temp
from typing import Union, Optional, AsyncGenerator
from pyrogram import types
from Script import script 
from datetime import date, datetime 
import pytz
from aiohttp import web
from plugins import web_server

import asyncio
from pyrogram import idle
from lazybot import LazyPrincessBot
from util.keepalive import ping_server
from lazybot.clients import initialize_clients

# --- SAFETY CHECK FOR MISSING VARIABLES ---
# This prevents the "NameError" if these are missing in info.py
ON_HEROKU = globals().get('ON_HEROKU', 'DYNO' in environ)
PORT = globals().get('PORT', 8080)
LOG_CHANNEL = globals().get('LOG_CHANNEL', None)  # Changed default to None
# ------------------------------------------

ppath = "plugins/*.py"
files = glob.glob(ppath)
LazyPrincessBot.start()
loop = asyncio.get_event_loop()


async def safe_send_to_log(message_text):
    """
    Safely send messages to LOG_CHANNEL with error handling.
    If LOG_CHANNEL is None or invalid, log to console instead.
    """
    if not LOG_CHANNEL:
        logging.info(f"[LOG_CHANNEL_DISABLED] {message_text}")
        return None
    
    try:
        return await LazyPrincessBot.send_message(
            chat_id=LOG_CHANNEL, 
            text=message_text
        )
    except PeerIdInvalid:
        logging.error(f"❌ Invalid LOG_CHANNEL ID: {LOG_CHANNEL}")
        logging.error("⚠️  Please fix LOG_CHANNEL in info.py. Bot needs to be added to the channel first!")
        logging.info(f"[LOG_MESSAGE] {message_text}")
        return None
    except ChannelInvalid:
        logging.error(f"❌ Invalid Channel: {LOG_CHANNEL}")
        logging.error("⚠️  Verify the LOG_CHANNEL ID is correct")
        logging.info(f"[LOG_MESSAGE] {message_text}")
        return None
    except FloodWait as e:
        logging.warning(f"FloodWait: Sleeping for {e.x} seconds")
        await asyncio.sleep(e.x)
        return await safe_send_to_log(message_text)
    except Exception as e:
        logging.error(f"❌ Error sending to LOG_CHANNEL: {e}")
        logging.info(f"[LOG_MESSAGE] {message_text}")
        return None


async def Lazy_start():
    print('\n')
    print('Initializing The Movie Provider Bot')
    bot_info = await LazyPrincessBot.get_me()
    LazyPrincessBot.username = bot_info.username
    
    # Initialize clients
    try:
        await initialize_clients()
    except Exception as e:
        logging.error(f"Error initializing clients: {e}")
    
    # Load plugins
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem.replace(".py", "")
            plugins_dir = Path(f"plugins/{plugin_name}.py")
            import_path = "plugins.{}".format(plugin_name)
            spec = importlib.util.spec_from_file_location(import_path, plugins_dir)
            load = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(load)
            sys.modules["plugins." + plugin_name] = load
            print("The Movie Provider Imported => " + plugin_name)
    
    # Start ping server if on Heroku
    if ON_HEROKU:
        asyncio.create_task(ping_server())

    # Get banned users and chats
    try:
        b_users, b_chats = await db.get_banned()
        temp.BANNED_USERS = b_users
        temp.BANNED_CHATS = b_chats
    except Exception as e:
        logging.error(f"Error getting banned users/chats: {e}")
        temp.BANNED_USERS = []
        temp.BANNED_CHATS = []
    
    # Ensure database indexes
    try:
        await Media.ensure_indexes()
    except Exception as e:
        logging.error(f"Error ensuring indexes: {e}")
    
    # Get bot info
    me = await LazyPrincessBot.get_me()
    temp.ME = me.id
    temp.U_NAME = me.username
    temp.B_NAME = me.first_name
    LazyPrincessBot.username = '@' + me.username
    
    logging.info(f"{me.first_name} with Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")
    logging.info(LOG_STR)
    
    try:
        logging.info(script.LOGO)
    except:
        pass
    
    # Send startup message to LOG_CHANNEL
    tz = pytz.timezone('Asia/Kolkata')
    today = date.today()
    now = datetime.now(tz)
    time = now.strftime("%H:%M:%S %p")
    
    startup_message = script.RESTART_TXT.format(today, time)
    await safe_send_to_log(startup_message)
    
    # Start web server
    try:
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()
        logging.info(f"Web server started on port {PORT}")
    except Exception as e:
        logging.error(f"Error starting web server: {e}")
    
    # Keep the bot running
    await idle()


if __name__ == '__main__':
    try:
        loop.run_until_complete(Lazy_start())
    except KeyboardInterrupt:
        logging.info('Service Stopped Bye 👋')
    except Exception as e:
        logging.error(f"Fatal error: {e}")
        import traceback
        traceback.print_exc()
        
