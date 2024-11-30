from aiogram import types

from keyboards.inlines import inline_webapp_kb
from loader import dp


@dp.message_handler(commands=['manage_groups'])
async def secret_web_app(message: types.Message):
    await message.answer(
        'Дотсуп к секретному ресурсу',
        reply_markup=inline_webapp_kb,
    )
