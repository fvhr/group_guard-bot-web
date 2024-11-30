from aiogram import types

from keyboards.inlines import create_manage_chat_ikb
from loader import dp, bot


@dp.callback_query_handler(lambda call: call.data.startswith('return_'))
async def _return(call: types.CallbackQuery):
    chat_id = call.data.split('_')[1]
    ikb = await create_manage_chat_ikb(chat_id)
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=ikb)
