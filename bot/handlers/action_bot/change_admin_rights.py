from aiogram import types

from filters.bot_actions_filters import GroupCustomFilters
from loader import dp, bot
from modules import ManageBotAction


@dp.my_chat_member_handler(GroupCustomFilters.CHANGE_ADMIN_RIGHTS)
async def add_bot_in_chat(update: types.ChatMemberUpdated):
    chat = await bot.get_chat(update.chat.id)
    await ManageBotAction.give_bot_admin_rights(chat)
