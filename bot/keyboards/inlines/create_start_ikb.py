from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def create_start_ikb(chats: list) -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup()
    for chat in chats:
        ikb.add(
            InlineKeyboardButton(
                text=chat['title'],
                callback_data=f'chat_{chat["id"]}',
            ),
        )
    return ikb
