from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def create_change_group(chat_id: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='Изменить фото📸',
                    callback_data=f'change_photo_{chat_id}'
                ),
                InlineKeyboardButton(
                    text='Изменить описание📋',
                    callback_data=f'change_description_{chat_id}'
                ),
            ],
            [
                InlineKeyboardButton(
                    text='Изменить название📜',
                    callback_data=f'change_tittle_{chat_id}'
                ),
            ],
            [
                InlineKeyboardButton(
                    text='⬅️Назад',
                    callback_data=f'return_{chat_id}'
                ),
            ],
        ]
    )


async def create_cancel_change_group_ikb(chat_id: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='Отмена❌',
                    callback_data=f'cancel_change_group_{chat_id}'
                ),

            ],

        ]
    )
