from aiogram import types
from aiogram.utils.exceptions import UserIsAnAdministratorOfTheChat, BadRequest

from handlers.personal_message.utils import get_chat_info
from keyboards.inlines import create_manage_chat_ikb
from loader import dp, bot
from modules.interaction_api import InteractionBackendAPI


@dp.callback_query_handler(lambda call: call.data.startswith('choose_this_'))
async def delete_this_chat(call: types.CallbackQuery):
    member_id, chat_id = call.data.split('_')[2:]
    chat = await bot.get_chat(chat_id)
    try:
        await bot.kick_chat_member(chat_id=chat_id, user_id=member_id)
        await InteractionBackendAPI.delete_users_chats(
            chat_id=chat_id,
            user_id=member_id,
        )
        await bot.edit_message_text(
            f'Пользователь успешно удалён из чата: {chat.title}✅',
            message_id=call.message.message_id,
            chat_id=call.message.chat.id,
        )
    except UserIsAnAdministratorOfTheChat:
        await bot.edit_message_text(
            f'Не удалось удалить пользователя из чата: {chat.title}❌\n'
            f'Причина: он администратор',
            message_id=call.message.message_id,
            chat_id=call.message.chat.id,
        )
    except BadRequest:
        await bot.edit_message_text(
            f'Не удалось удалить пользователя из чата: {chat.title}❌\n'
            f'Причина: он не состоит в чате',
            message_id=call.message.message_id,
            chat_id=call.message.chat.id,
        )

    message_send, bot_is_admin = await get_chat_info(chat_id)
    if bot_is_admin:
        ikb = await create_manage_chat_ikb(chat_id)
        await call.message.answer(
            message_send,
            parse_mode='HTML',
            reply_markup=ikb,
        )
    else:
        await call.message.answer(message_send, parse_mode='HTML')
