import logging

import aiohttp

from loader import settings
from shemas import AvatarUserInfo

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)


class InteractionBackendAPI:
    BASE_URL = settings.BASE_API_BACKEND_URL

    @classmethod
    async def chats_create(cls, data: dict) -> dict:
        endpoint = f'{cls.BASE_URL}/chats/'
        async with aiohttp.ClientSession() as session:
            async with session.post(endpoint, json=data) as response:
                logging.info(f'post from {endpoint}: {response.status}')
                return await response.json()

    @classmethod
    async def check_change_rights(cls, chat_id: int) -> bool:
        endpoint = f'{cls.BASE_URL}/chats/{chat_id}/'
        async with aiohttp.ClientSession() as session:
            async with session.get(endpoint) as response:
                logging.info(f'get from {endpoint}: {response.status}')
                js = await response.json()
                if 'id' in js:
                    return True
                return False

    @classmethod
    async def chats_patch(cls, chat_id: int, fields: dict) -> None:
        endpoint = f'{cls.BASE_URL}/chats/{chat_id}/'
        async with aiohttp.ClientSession() as session:
            async with session.patch(endpoint, json=fields) as response:
                logging.info(f'patch from {endpoint}: {response.status}')

    @classmethod
    async def chats_delete(cls, chat_id: int) -> None:
        endpoint = f'{cls.BASE_URL}/chats/{chat_id}/'
        async with aiohttp.ClientSession() as session:
            async with session.delete(endpoint) as response:
                logging.info(f'delet from {endpoint}: {response.status}')

    @classmethod
    async def user_create(cls, data: dict) -> None:
        endpoint = f'{cls.BASE_URL}/users/'
        avatar_user_info = await AvatarUserInfo.from_chat(data['id'])
        data['photo_url'] = avatar_user_info.avatar_url
        async with aiohttp.ClientSession() as session:
            async with session.post(endpoint, json=data) as response:
                logging.info(f'post from {endpoint}: {response.status}')

    @classmethod
    async def user_chats_create(cls, data: dict) -> None:
        endpoint = f'{cls.BASE_URL}/users-chats/'
        async with aiohttp.ClientSession() as session:
            async with session.post(endpoint, json=data) as response:
                logging.info(f'post from {endpoint}: {response.status}')

    @classmethod
    async def delete_users_chats(cls, user_id: int, chat_id: int) -> None:
        endpoint = f'{cls.BASE_URL}/chats/{chat_id}/delete-user/'
        async with aiohttp.ClientSession() as session:
            async with session.delete(
                endpoint,
                params={'user_id': user_id},
            ) as response:
                logging.info(f'delet from {endpoint}: {response.status}')

    @classmethod
    async def exist_user(cls, user_id: int) -> bool:
        endpoint = f'{cls.BASE_URL}/users/{user_id}/'
        async with aiohttp.ClientSession() as session:
            async with session.get(endpoint) as response:
                logging.info(f'get from {endpoint}: {response.status}')
                js = await response.json()
                if 'id' in js:
                    return True
                return False

    @classmethod
    async def change_admin_status(
        cls,
        chat_id: int,
        user_id: int,
        is_admin: bool,
    ) -> None:
        endpoint = f'{cls.BASE_URL}/chats/{chat_id}/update-is-admin/'
        async with aiohttp.ClientSession() as session:
            async with session.patch(
                endpoint,
                params={'user_id': user_id},
                json={'is_admin': is_admin},
            ) as response:
                logging.info(f'patch from {endpoint}: {response.status}')

    @classmethod
    async def check_user_is_admin(cls, user_id: int) -> dict:
        endpoint = f'{cls.BASE_URL}/users/{user_id}/admin-chats/'
        async with aiohttp.ClientSession() as session:
            async with session.get(endpoint) as response:
                logging.info(f'get from {endpoint}: {response.status}')
                return await response.json()

    @classmethod
    async def get_users_chat(cls, chat_id: str) -> dict:
        endpoint = f'{cls.BASE_URL}/chats/{chat_id}/users/'
        async with aiohttp.ClientSession() as session:
            async with session.get(endpoint) as response:
                logging.info(f'get from {endpoint}: {response.status}')
                return await response.json()

    @classmethod
    async def get_chat(cls, chat_id: str) -> dict:
        endpoint = f'{cls.BASE_URL}/chats/{chat_id}/'
        async with aiohttp.ClientSession() as session:
            async with session.get(endpoint) as response:
                logging.info(f'get from {endpoint}: {response.status}')
                return await response.json()

    @classmethod
    async def check_user(cls, user: dict, chat_id: int) -> None:
        endpoint = f'{cls.BASE_URL}/chats/{chat_id}/check-user/'
        async with aiohttp.ClientSession() as session:
            async with session.post(endpoint, data=user) as response:
                logging.info(f'post from {endpoint}: {response.status}')

    @classmethod
    async def member_chat(cls, user_id: int) -> list:
        endpoint = f'{cls.BASE_URL}/users/{user_id}/member-chats/'
        async with aiohttp.ClientSession() as session:
            async with session.get(endpoint) as response:
                logging.info(f'get from {endpoint}: {response.status}')
                js = await response.json()
                return js

    @classmethod
    async def user_is_staff(cls, user_id: int) -> bool:
        endpoint = f'{cls.BASE_URL}/users/{user_id}/'
        async with aiohttp.ClientSession() as session:
            async with session.get(endpoint) as response:
                js = await response.json()
                logging.info(f'get from {endpoint}: {response.status}')
                return js['is_staff']
