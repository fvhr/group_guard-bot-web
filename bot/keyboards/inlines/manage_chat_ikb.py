from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def create_manage_chat_ikb(chat_id: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='Изменение группы⚙️',
                    callback_data=f'change_group_{chat_id}'
                ),
                InlineKeyboardButton(
                    text='Удаление участника❌',
                    callback_data=f'delete_member_{chat_id}'
                ),
            ]
        ]
    )
