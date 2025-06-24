import random
import string


from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InputMediaPhoto, Message
from pytgcalls.exceptions import NoActiveGroupCall


import config
from ShrutiMusic import Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app
from ShrutiMusic.core.call import Aviax
from ShrutiMusic.utils import seconds_to_min, time_to_seconds
from ShrutiMusic.utils.channelplay import get_channeplayCB
from ShrutiMusic.utils.decorators.language import languageCB
from ShrutiMusic.utils.decorators.play import PlayWrapper
from ShrutiMusic.utils.formatters import formats
from ShrutiMusic.utils.inline import (
    botplaylist_markup,
    livestream_markup,
    playlist_markup,
    slider_markup,
    track_markup,
)
from ShrutiMusic.utils.logger import play_logs
from ShrutiMusic.utils.stream.stream import stream
from config import BANNED_USERS, lyrical




@app.on_message(
    filters.command(
        [
            "play",
            "vplay",
            "cplay",
            "cvplay",
            "playforce",
            "vplayforce",
            "cplayforce",
            "cvplayforce",
        ]
    )
    & filters.group
    & ~BANNED_USERS
)
@PlayWrapper
async def play_commnd(
    client,
    message: Message,
    _,
    chat_id,
    video,
    channel,
    playmode,
    url,
  
  fplay,
