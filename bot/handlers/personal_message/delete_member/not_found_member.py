from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inlines import create_cancel_delete_member, choose_variant
from loader import dp, bot
from states.delete_member import DeleteMember


@dp.callback_query_handler(lambda call: call.data.startswith('not_found_'))
async def not_found_member(call: types.CallbackQuery, state: FSMContext):
    chat_id = call.data.split('_')[2]
    await state.update_data(
        chat_id=chat_id,
        message_id=call.message.message_id,
    )
    await DeleteMember.tg_user_id.set()
    await bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text='Пришлите telegram id пользователя которого хотите удалить.',
    )

    ikb = await create_cancel_delete_member(chat_id)
    await bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=ikb,
    )


@dp.message_handler(
    content_types=types.ContentType.TEXT,
    state=DeleteMember.tg_user_id,
)
async def state_username(
    message: types.Message,
    state: FSMContext,
):
    if message.text.isdigit():
        data = await state.get_data()
        chat_id = data['chat_id']
        message_id = data['message_id']
        ikb = await choose_variant(message.text, chat_id)
        await bot.delete_message(
            chat_id=message.chat.id,
            message_id=message_id,
        )
        await message.answer(
            'Выберите откуда хотите удалить пользователя',
            reply_markup=ikb,
        )
        await state.finish()
    else:
        ikb = await create_cancel_delete_member(message.chat.id)
        await message.answer(
            'Telegram user id должен быть числом, попробуйте снова.',
            reply_markup=ikb,
        )
