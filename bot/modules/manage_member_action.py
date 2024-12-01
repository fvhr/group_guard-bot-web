from modules.interaction_api import InteractionBackendAPI


class ManageMemberAction:
    @staticmethod
    async def add_member_in_chat(member: dict, chat_id: int) -> None:
        if not await InteractionBackendAPI.exist_user(member['id']):
            await InteractionBackendAPI.user_create(member)
        await InteractionBackendAPI.user_chats_create(
            data={'user': member['id'], 'chat': chat_id},
        )

    @staticmethod
    async def give_member_admin_rights(user: dict, chat_id: int) -> None:
        if not await InteractionBackendAPI.exist_user(user['id']):
            await InteractionBackendAPI.user_create(user)
        await InteractionBackendAPI.change_admin_status(
            chat_id,
            user['id'],
            is_admin=True,
        )

    @staticmethod
    async def kicked_member_chat(user_id: int, chat_id: int) -> None:
        await InteractionBackendAPI.delete_users_chats(user_id, chat_id)

    @staticmethod
    async def remove_member_admin_rights(user: dict, chat_id: int) -> None:
        if not await InteractionBackendAPI.exist_user(user['id']):
            await InteractionBackendAPI.user_create(user)
        await InteractionBackendAPI.change_admin_status(
            chat_id,
            user['id'],
            is_admin=False,
        )
