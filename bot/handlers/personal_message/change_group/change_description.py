from aiogram import types
from aiogram.dispatcher import FSMContext

from handlers.personal_message.utils import get_chat_info
from keyboards.inlines import (
    create_cancel_change_group_ikb,
    create_manage_chat_ikb,
)
from loader import dp, bot
from modules.interaction_api import InteractionBackendAPI
from states.change_group import ChangeGroup


@dp.callback_query_handler(
    lambda call: call.data.startswith('change_description_'),
)
async def change_description(call: types.CallbackQuery, state: FSMContext):
    chat_id = call.data.split('_')[2]
    await state.update_data(
        chat_id=chat_id,
        message_id=call.message.message_id,
    )
    await ChangeGroup.change_description.set()

    await bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text='Пришлите новое описание для чата.',
    )

    ikb = await create_cancel_change_group_ikb(chat_id)
    await bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=ikb,
    )


@dp.message_handler(
    content_types=types.ContentType.TEXT,
    state=ChangeGroup.change_description,
)
async def save_and_update_description(
    message: types.Message,
    state: FSMContext,
):
    data = await state.get_data()
    chat_id = data.get('chat_id')
    new_description = message.text
    await bot.set_chat_description(
        chat_id=chat_id,
        description=new_description,
    )
    await InteractionBackendAPI.chats_patch(
        chat_id,
        {'description': new_description},
    )
    message_id = data.get('message_id')
    await bot.delete_message(chat_id=message.chat.id, message_id=message_id)

    message_send, bot_is_admin = await get_chat_info(chat_id)
    if bot_is_admin:
        ikb = await create_manage_chat_ikb(chat_id)
        await message.answer(message_send, parse_mode='HTML', reply_markup=ikb)
    else:
        await message.answer(message_send, parse_mode='HTML')
    await state.finish()
