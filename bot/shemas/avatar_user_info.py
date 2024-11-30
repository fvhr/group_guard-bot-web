from pydantic import BaseModel

from loader import bot, settings


class AvatarUserInfo(BaseModel):
    avatar_url: str

    @classmethod
    async def from_chat(cls, user_id: int) -> 'AvatarUserInfo':
        """Метод для получения ссылки на аватарку чата."""
        photos = await bot.get_user_profile_photos(user_id=user_id)
        if photos.total_count > 0:
            photo = photos.photos[0][-1]
            file_info = await bot.get_file(photo.file_id)
            avatar_url = (
                f'https://api.telegram.org/file/bot'
                f'{settings.BOT_TOKEN}/{file_info.file_path}'
            )
        else:
            avatar_url = settings.BASE_AVATAR_PATH
        return cls(avatar_url=avatar_url)
