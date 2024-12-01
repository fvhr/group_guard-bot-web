from aiogram import types

from keyboards.inlines import choose_variant
from loader import dp, bot


@dp.callback_query_handler(lambda call: call.data.startswith('del_member_'))
async def del_member(call: types.CallbackQuery):
    member_id, chat_id = call.data.split('_')[2:]
    message_id = call.message.message_id
    ikb = await choose_variant(member_id, chat_id)
    await bot.delete_message(
        chat_id=call.message.chat.id,
        message_id=message_id,
    )
    await call.message.answer(
        'Выберите откуда хотите удалить пользователя',
        reply_markup=ikb,
    )
