from aiogram import types

from filters.bot_actions_filters import GroupCustomFilters
from loader import dp, bot
from modules import ManageBotAction


@dp.my_chat_member_handler(GroupCustomFilters.ADD_BOT_IN_CHAT)
async def add_bot_in_chat(update: types.ChatMemberUpdated):
    chat = await bot.get_chat(update.chat.id)
    await ManageBotAction.add_bot_in_chat(chat)
