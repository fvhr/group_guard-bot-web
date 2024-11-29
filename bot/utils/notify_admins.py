from aiogram import Dispatcher

from utils import settings


async def on_startup_notify(dp: Dispatcher):
    await dp.bot.send_message(
        chat_id=settings.ADMIN_TG_UUID,
        text='Bot Started',
    )
