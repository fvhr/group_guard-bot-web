from typing import Callable

from aiogram import types


class GroupCustomFilters:
    ADD_BOT_IN_CHAT: Callable[[types.ChatMemberUpdated], bool] = (
        lambda update: update.new_chat_member.status
        == types.ChatMemberStatus.MEMBER
    )

    CHANGE_ADMIN_RIGHTS: Callable[[types.ChatMemberUpdated], bool] = (
        lambda update: update.new_chat_member.status
        == types.ChatMemberStatus.ADMINISTRATOR
    )

    REMOVE_BOT_IN_CHAT: Callable[[types.ChatMemberUpdated], bool] = (
        lambda update: update.new_chat_member.status
        == types.ChatMemberStatus.LEFT
    )
