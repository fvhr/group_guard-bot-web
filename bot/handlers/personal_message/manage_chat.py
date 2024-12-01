from aiogram import types

from handlers.personal_message.utils import get_chat_info
from keyboards.inlines import create_manage_chat_ikb
from loader import dp


@dp.callback_query_handler(lambda call: call.data.startswith('chat_'))
async def manage_chat(call: types.CallbackQuery):
    chat_id = call.data.split('_')[1]
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
