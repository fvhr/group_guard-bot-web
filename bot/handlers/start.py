from aiogram import types

from keyboards.inlines import create_start_ikb
from loader import dp
from modules.interaction_api import InteractionBackendAPI


@dp.message_handler(
    lambda message: message.chat.type == 'private',
    commands=['start'],
)
async def start(message: types.Message):
    response = await InteractionBackendAPI.check_user_is_admin(
        message.from_user.id,
    )
    if len(response) > 0:
        ikb = await create_start_ikb(response)
        await message.answer(
            '👋 Добро пожаловать! Я бот для '
            'управления корпоративными группами.\n\n'
            '📋 Вот что я могу:\n'
            '1️⃣ Отслеживать изменения в группе:\n'
            '   - Название группы\n'
            '   - Фото группы\n'
            '   - Список администраторов группы\n\n'
            '2️⃣ Управлять участниками:\n'
            '   - Удаление участников\n'
            '   - Ограничение доступа\n\n'
            '⚠️ Для корректной работы бота в группе предоставьте '
            'ему права администратора.',
            reply_markup=ikb,
        )
    else:
        await message.answer(
            'Вы не являетесь администратором ни одного из корпоративных чатов',
        )
