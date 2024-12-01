from aiogram.types.chat import Chat

from loader import bot
from modules.interaction_api import InteractionBackendAPI
from shemas import AvatarInfo, AdminInfo, GroupInfo


class ManageBotAction:

    @staticmethod
    async def add_bot_in_chat(chat: Chat) -> None:
        # Получаем администраторов
        admin_info = await AdminInfo.from_chat(chat)
        if await InteractionBackendAPI.check_change_rights(chat.id):
            await InteractionBackendAPI.chats_patch(
                chat.id,
                fields={
                    'id': chat.id,
                    'title': chat.title,
                    'bot_is_admin': False,
                },
            )
            return
        # Получаем аватарку
        avatar_url = await AvatarInfo.from_chat(chat)

        group_info = GroupInfo(
            id=chat.id,
            title=chat.title,
            description=chat.description,
            avatar_url=avatar_url.avatar_url,
        )

        data = group_info.model_dump()
        await InteractionBackendAPI.chats_create(data)

        for admin in admin_info.admins:
            user = await bot.get_chat_member(chat_id=chat.id, user_id=admin)
            if not await InteractionBackendAPI.exist_user(user.user.id):
                await InteractionBackendAPI.user_create(dict(user.user))
            await InteractionBackendAPI.user_chats_create(
                {'user': user.user.id, 'chat': chat.id, 'is_admin': True},
            )

    @staticmethod
    async def remove_bot_in_chat(chat: Chat) -> None:
        await InteractionBackendAPI.chats_delete(chat.id)

    @staticmethod
    async def give_bot_admin_rights(chat: Chat) -> None:
        admin_info = await AdminInfo.from_chat(chat)
        try:
            chat_invite_link = await chat.export_invite_link()
        except Exception:
            chat_invite_link = None
        for admin in admin_info.admins:
            user = await bot.get_chat_member(chat_id=chat.id, user_id=admin)
            if not user.user.is_bot:
                if not await InteractionBackendAPI.exist_user(user.user.id):
                    await InteractionBackendAPI.user_create(dict(user.user))
                await InteractionBackendAPI.change_admin_status(
                    chat.id,
                    user.user.id,
                    is_admin=True,
                )
        await InteractionBackendAPI.chats_patch(
            chat.id,
            fields={
                'id': chat.id,
                'title': chat.title,
                'bot_is_admin': True,
                'url': chat_invite_link,
            },
        )
