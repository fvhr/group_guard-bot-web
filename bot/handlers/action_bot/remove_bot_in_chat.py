from aiogram import types

from filters.bot_actions_filters import GroupCustomFilters
from loader import dp
from modules import ManageBotAction


@dp.my_chat_member_handler(GroupCustomFilters.REMOVE_BOT_IN_CHAT)
async def add_bot_in_chat(update: types.ChatMemberUpdated):
    chat = update.chat
    await ManageBotAction.remove_bot_in_chat(chat)
