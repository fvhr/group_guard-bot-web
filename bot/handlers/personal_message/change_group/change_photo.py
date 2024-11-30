import io

import aiohttp
from aiogram import types
from aiogram.dispatcher import FSMContext

from handlers.personal_message.utils import get_chat_info
from keyboards.inlines import (
    create_cancel_change_group_ikb,
    create_manage_chat_ikb,
)
from loader import dp, bot, settings
from states.change_group import ChangeGroup


@dp.callback_query_handler(lambda call: call.data.startswith('change_photo_'))
async def change_photo(call: types.CallbackQuery, state: FSMContext):
    chat_id = call.data.split('_')[2]
    await state.update_data(
        chat_id=chat_id,
        message_id=call.message.message_id,
    )
    await ChangeGroup.change_photo.set()

    await bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text='Пришлите новое фото для чата.',
    )

    ikb = await create_cancel_change_group_ikb(chat_id)
    await bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=ikb,
    )


@dp.message_handler(
    content_types=types.ContentType.PHOTO,
    state=ChangeGroup.change_photo,
)
async def save_and_update_photo(message: types.Message, state: FSMContext):
    data = await state.get_data()
    chat_id = data.get('chat_id')
    photo = message.photo[-1]
    file_id = photo.file_id
    file_info = await bot.get_file(file_id)
    file_path = file_info.file_path
    file_url = f'{settings.BASE_API_TG_URL}{settings.BOT_TOKEN}/{file_path}'
    async with aiohttp.ClientSession() as session:
        async with session.get(file_url) as response:
            if response.status == 200:
                photo_bytes = await response.read()
                input_file = types.InputFile(
                    io.BytesIO(photo_bytes),
                    filename='new_chat_photo.jpg',
                )
                await bot.set_chat_photo(chat_id=chat_id, photo=input_file)
    message_id = data.get('message_id')
    await bot.delete_message(chat_id=message.chat.id, message_id=message_id)

    message_send, bot_is_admin = await get_chat_info(chat_id)
    if bot_is_admin:
        ikb = await create_manage_chat_ikb(chat_id)
        await message.answer(message_send, parse_mode='HTML', reply_markup=ikb)
    else:
        await message.answer(message_send, parse_mode='HTML')
    await state.finish()
