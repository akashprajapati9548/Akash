from pyrogram.types import InlineKeyboardButton
import config
from ShrutiMusic import app

def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥀ᴀᴅᴅ ᴍᴇ ɪɴ ɴᴇᴡ ɢʀᴏᴜᴘ🥀", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text="🍷Sᴜᴘᴘᴏʀᴛ🍷", url=config.SUPPORT_GROUP),
        ]
    ]
    return buttons

def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥀ᴀᴅᴅ ᴍᴇ ɪɴ ɴᴇᴡ ɢʀᴏᴜᴘ🥀",
                url=f"https://t.me/{app.username}?startgroup=true"
            )
        ],
        [
            InlineKeyboardButton(text="Sᴜᴘᴘᴏʀᴛ", url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text="Dᴇᴠᴇʟᴏᴘᴇʀ", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="Gʀᴏᴜᴘ", url=config.SUPPORT_GROUP),
        ],
        [
            InlineKeyboardButton(text="🫧Hᴇʟᴘ Aɴᴅ Cᴏᴍᴍᴀɴᴅs🫧", callback_data="settings_back_helper"),
        ]
    ]
    return buttons
