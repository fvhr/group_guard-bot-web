from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo,
)

from loader import settings

inline_webapp_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Управление чатами',
                web_app=WebAppInfo(url=settings.WEB_APP_URL),
            ),
        ],
    ],
)
