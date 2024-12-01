from aiogram.types import (
    WebAppInfo,
    ReplyKeyboardMarkup,
    KeyboardButton,
)

from loader import settings

webapp_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text='Управление чатами',
                web_app=WebAppInfo(url=settings.WEB_APP_URL),
            ),
        ],
    ],
    resize_keyboard=True,
)
