from typing import List

from aiogram.types.chat import Chat
from aiogram.utils.exceptions import ChatAdminRequired
from pydantic import BaseModel

from loader import bot


class AdminInfo(BaseModel):
    admins: List[int] = []

    @classmethod
    async def from_chat(cls, chat: Chat) -> 'AdminInfo':
        """Метод для получения списка администраторов чата."""
        try:
            members = []
            chat_members = await bot.get_chat_administrators(chat.id)
            for member in chat_members:
                members.append(member.user.id)
            return cls(admins=members)
        except ChatAdminRequired:
            return cls(admins=[])
