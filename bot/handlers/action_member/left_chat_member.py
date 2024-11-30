from aiogram import types

from loader import dp
from modules import ManageMemberAction


@dp.message_handler(content_types=[types.ContentType.LEFT_CHAT_MEMBER])
async def left_user(message: types.Message):
    member = message.left_chat_member
    if not member['is_bot']:
        await ManageMemberAction.kicked_member_chat(dict(member))
