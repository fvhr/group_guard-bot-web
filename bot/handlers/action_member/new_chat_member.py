from aiogram import types

from loader import dp
from modules import ManageMemberAction


@dp.message_handler(content_types=[types.ContentType.NEW_CHAT_MEMBERS])
async def new_user(message: types.Message):
    member = message.new_chat_members[0]
    if not member['is_bot']:
        await ManageMemberAction.add_member_in_chat(
            dict(member),
            message.chat.id,
        )
