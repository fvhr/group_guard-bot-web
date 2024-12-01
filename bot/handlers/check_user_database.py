from aiogram import types

from loader import dp
from modules.interaction_api import InteractionBackendAPI


@dp.message_handler(content_types=['text'])
async def check_user_database(message: types.Message):
    await InteractionBackendAPI.check_user(
        dict(message.from_user),
        message.chat.id,
    )
