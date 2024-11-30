from aiogram.types.chat import Chat

from modules.interaction_api import InteractionBackendAPI
from shemas import AvatarInfo


class ManageGroupAction:
    @staticmethod
    async def change_photo_group(chat: Chat) -> None:
        avatar_url = await AvatarInfo.from_chat(chat)
        await InteractionBackendAPI.chats_patch(
            chat.id,
            fields={
                'id': chat.id,
                'title': chat.title,
                'avatar_url': avatar_url.avatar_url,
            },
        )

    @staticmethod
    async def change_name_group(chat: Chat) -> None:
        await InteractionBackendAPI.chats_patch(
            chat.id, fields={'id': chat.id, 'title': chat.title}
        )
