import json

from aiogram import types
from aiogram.utils.exceptions import BadRequest, UserIsAnAdministratorOfTheChat

from keyboards import webapp_kb
from loader import dp, bot
from modules.interaction_api import InteractionBackendAPI


@dp.message_handler(commands=['manage_groups'])
async def secret_web_app(message: types.Message):
    if await InteractionBackendAPI.user_is_staff(message.from_user.id):
        await message.answer(
            'Доступ к секретному ресурсу',
            reply_markup=webapp_kb,
        )


@dp.message_handler(content_types=types.ContentType.WEB_APP_DATA)
async def get_data(webappmes: types.WebAppData):
    data = json.loads(webappmes.web_app_data.data)
    if type(data['chat_id']) is int:
        try:
            await bot.kick_chat_member(chat_id=data['chat_id'], user_id=int(data['user_id']))
            await InteractionBackendAPI.delete_users_chats(
                chat_id=data['chat_id'],
                user_id=data['user_id'],
            )
        except BadRequest:
            pass
    else:
        chats = await InteractionBackendAPI.member_chat(data['user_id'])
        for chat in chats:
            await bot.kick_chat_member(chat_id=chat['id'], user_id=data['user_id'])
            await InteractionBackendAPI.delete_users_chats(
                chat_id=chat['id'],
                user_id=data['user_id'],
            )
