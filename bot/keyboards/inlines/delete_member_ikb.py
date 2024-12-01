from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def create_delete_member_ikb(
    members: list,
    chat_id: str,
) -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup()
    row = []
    for index, member in enumerate(members, start=1):
        user = member['user']
        button = InlineKeyboardButton(
            text=user['username'] if user['username'] else user['first_name'],
            callback_data=f'del_member_{user["id"]}_{chat_id}',
        )
        row.append(button)
        if len(row) == 2 or index == len(members):
            ikb.row(*row)
            row = []
    ikb.add(
        InlineKeyboardButton(
            text='Username нет в списке❌🔎',
            callback_data=f'not_found_{chat_id}',
        ),
    )
    ikb.add(
        InlineKeyboardButton(
            text='⬅️Назад',
            callback_data=f'return_{chat_id}',
        ),
    )

    return ikb


async def create_cancel_delete_member(chat_id: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='Отмена❌',
                    callback_data=f'cancel_delete_member_{chat_id}',
                ),
            ],
        ],
    )


async def choose_variant(username: str, chat_id: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='Удалить с этого чата',
                    callback_data=f'choose_this_{username}_{chat_id}',
                ),
                InlineKeyboardButton(
                    text='Удалить со всех чатов',
                    callback_data=f'choose_all_{username}_{chat_id}',
                ),
            ],
        ],
    )
