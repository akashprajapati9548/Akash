from pyrogram.types import InlineKeyboardButton
import config
from ShrutiMusic import app

def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=["S_B_2"], url=config.SUPPORT_GROUP),
        ]
    ]
    return buttons

def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true"
            )
        ],
        [
            InlineKeyboardButton(text=["E_X_1"], url="https://github.com/NoxxOP/ShrutiMusic"),
            InlineKeyboardButton(text=["S_B_5"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=["S_B_2"], url=config.SUPPORT_GROUP),
        ],
        [
            InlineKeyboardButton(text=["S_B_4"], callback_data="settings_back_helper"),
        ]
    ]
    return buttons
