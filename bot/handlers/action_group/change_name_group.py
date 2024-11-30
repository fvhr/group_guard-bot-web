from aiogram import types

from loader import bot, dp
from modules import ManageGroupAction


@dp.message_handler(content_types=types.ContentType.NEW_CHAT_TITLE)
async def change_photo_group(message: types.Message):
    chat = await bot.get_chat(message.chat.id)
    await ManageGroupAction.change_name_group(chat)
