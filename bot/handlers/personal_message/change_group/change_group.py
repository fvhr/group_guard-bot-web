from keyboards.inlines import create_change_group
from loader import dp, bot
from aiogram import types


@dp.callback_query_handler(lambda call: call.data.startswith('change_group_'))
async def change_group(call: types.CallbackQuery):
    chat_id = call.data.split('_')[2]
    ikb = await create_change_group(chat_id)
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    await bot.edit_message_reply_markup(
        chat_id=chat_id,
        message_id=message_id,
        reply_markup=ikb,
    )
