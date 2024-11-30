from aiogram.types.chat import Chat
from pydantic import BaseModel

from loader import bot, settings


class AvatarInfo(BaseModel):
    avatar_url: str

    @classmethod
    async def from_chat(cls, chat: Chat) -> 'AvatarInfo':
        """Метод для получения ссылки на аватарку чата."""
        if chat.photo:
            file = await bot.get_file(chat.photo.big_file_id)
            file_path = file.file_path
            avatar_url = (
                f'{settings.BASE_API_TG_URL}{settings.BOT_TOKEN}/{file_path}'
            )
        else:
            avatar_url = settings.BASE_AVATAR_PATH
        return cls(avatar_url=avatar_url)
