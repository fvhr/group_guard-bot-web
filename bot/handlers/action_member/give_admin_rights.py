from aiogram.types import ChatMemberUpdated

from loader import dp
from modules import ManageMemberAction


@dp.chat_member_handler(
    lambda update: update.new_chat_member.status == 'administrator',
)
async def give_admin_rights(update: ChatMemberUpdated):
    user = update.new_chat_member.user
    chat_id = update.chat.id
    await ManageMemberAction.give_member_admin_rights(dict(user), chat_id)
