from aiogram import types

from keyboards.inlines import create_delete_member_ikb
from loader import dp, bot
from modules.interaction_api import InteractionBackendAPI


@dp.callback_query_handler(lambda call: call.data.startswith('delete_member_'))
async def delete_member(call: types.CallbackQuery):
    chat_id = call.data.split('_')[2]
    response = await InteractionBackendAPI.get_users_chat(chat_id)
    no_admins_users = list(filter(lambda x: not x['is_admin'], response))
    ikb = await create_delete_member_ikb(no_admins_users, chat_id)
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    await bot.edit_message_reply_markup(
        chat_id=chat_id,
        message_id=message_id,
        reply_markup=ikb,
    )
