from django.test import TestCase
from .models import User, Chat, UsersChats


class APITestCase(TestCase):
    def setUp(self) -> None:
        self.url = 'http://localhost/api/'

        self.user1 = User.objects.create_user('u1', None, 'u1', id=1, is_premium=True)
        self.user2 = User.objects.create_user('u2', None, 'u2', id=2)

        self.chat1 = Chat.objects.create(id=-1, title='c1')
        self.chat2 = Chat.objects.create(id=-2, title='c2')

    # def test_user_create(self):
    #     pk = 3
    #     rsp = self.client.post(f'{self.url}users/', {'id': pk})
    #     self.assertEqual(rsp.data['id'], pk)
    #
    # def test_users_chats_bulk_create_and_delete(self):
    #     self.assertEqual(self.user1.chats.count(), 0)
    #
    #     rsp = self.client.post(
    #         f'{self.url}chats/-1/bulk-add/',
    #         {'user_ids': [1, 2]},
    #         content_type='application/json'
    #     )
    #     rsp = self.client.post(
    #         f'{self.url}chats/-2/bulk-add/',
    #         {'user_ids': [1, 2]},
    #         content_type='application/json'
    #     )
    #     self.assertEqual(self.user1.chats.count(), 2)
    #     self.assertEqual(self.user2.chats.count(), 2)
    #
    #     rsp = self.client.post(
    #         f'{self.url}users/1/bulk-delete/',
    #         {'chat_ids': [-1, -2]},
    #         content_type='application/json'
    #     )
    #     self.assertEqual(self.user1.chats.count(), 0)
    #     self.assertEqual(self.user2.chats.count(), 2)
    #
    # def test_get_user_admin_chats(self):
    #     UsersChats.objects.create(user=self.user1, chat=self.chat1, is_admin=True)
    #     UsersChats.objects.create(user=self.user1, chat=self.chat2, is_admin=False)
    #
    #     rsp = self.client.get(f'{self.url}users/1/admin-chats/')
    #     print(rsp.data)
    #     self.assertEqual(len(rsp.data), 1)
    #
    # def test_get_chat_users(self):
    #     UsersChats.objects.create(user=self.user1, chat=self.chat1, is_admin=True)
    #     UsersChats.objects.create(user=self.user2, chat=self.chat1, is_admin=False)
    #
    #     rsp = self.client.get(f'{self.url}chats/-1/users/')
    #     print("users ", rsp.data)

    def test_update_is_admin(self):
        UsersChats.objects.create(user=self.user1, chat=self.chat1, is_admin=False)
        rsp = self.client.patch(
            f'{self.url}chats/-1/update-is-admin/?user_id=1',
            {'is_admin': False},
            content_type='application/json'
        )
        print(rsp.data)
