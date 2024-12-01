from aiogram import types
from aiogram.dispatcher import FSMContext

from handlers.personal_message.utils import get_chat_info
from keyboards.inlines import create_manage_chat_ikb
from loader import dp, bot
from states.change_group import ChangeGroup
from states.delete_member import DeleteMember


@dp.callback_query_handler(
    lambda call: call.data.startswith('cancel_delete_member_'),
    state=DeleteMember,
)
async def cancel_change_group(call: types.CallbackQuery, state: FSMContext):
    chat_id = call.data.split('_')[3]
    message_send, bot_is_admin = await get_chat_info(chat_id)
    await bot.delete_message(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
    )
    if bot_is_admin:
        ikb = await create_manage_chat_ikb(chat_id)
        await call.message.answer(
            message_send,
            parse_mode='HTML',
            reply_markup=ikb,
        )
    else:
        await call.message.answer(message_send, parse_mode='HTML')
    await state.finish()
