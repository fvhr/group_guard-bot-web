from aiogram import types
from aiogram.utils.exceptions import UserIsAnAdministratorOfTheChat, BadRequest

from handlers.personal_message.utils import get_chat_info
from keyboards.inlines import create_manage_chat_ikb
from loader import dp, bot
from modules.interaction_api import InteractionBackendAPI


@dp.callback_query_handler(lambda call: call.data.startswith('choose_all_'))
async def delete_all_chat(call: types.CallbackQuery):
    messages = []
    member_id, chat_id = call.data.split('_')[2:]
    chats = await InteractionBackendAPI.check_user_is_admin(call.from_user.id)
    for chat in chats:
        if chat['bot_is_admin']:
            try:
                await bot.kick_chat_member(
                    chat_id=chat['id'],
                    user_id=member_id,
                )
                await InteractionBackendAPI.delete_users_chats(
                    chat_id=chat['id'],
                    user_id=member_id,
                )
                messages.append(
                    f'Пользователь успешно удалён из чата: {chat["title"]}✅',
                )
            except UserIsAnAdministratorOfTheChat:
                messages.append(
                    f'Не удалось удалить пользователя из '
                    f'чата: {chat["title"]}❌\n'
                    f'Причина: он администратор',
                )
            except BadRequest:
                messages.append(
                    f'Не удалось удалить пользователя из чата: '
                    f'{chat["title"]}❌\n'
                    f'Причина: он не состоит в чате',
                )
        else:
            messages.append(
                f'Не удалось удалить пользователя из чата: '
                f'{chat["title"]}❌\n'
                f'Причина: бот не администратор',
            )
    await call.message.answer('\n'.join(messages))

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
