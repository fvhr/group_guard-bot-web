from django.test import TestCase
from .models import User, Chat, UsersChats


class APITestCase(TestCase):
    def setUp(self) -> None:
        self.url = 'http://localhost/api/'

        self.user1 = User.objects.create_user(
            'u1', None, 'u1', id=1, is_premium=True
        )
        self.user2 = User.objects.create_user('u2', None, 'u2', id=2)

        self.chat1 = Chat.objects.create(id=-1, title='c1')
        self.chat2 = Chat.objects.create(id=-2, title='c2')

    def test_user_create(self):
        pk = 3
        rsp = self.client.post(f'{self.url}users/', {'id': pk})
        self.assertEqual(rsp.data['id'], pk)

    def test_users_chats_bulk_create_and_delete(self):
        self.assertEqual(self.user1.chats.count(), 0)

        self.client.post(
            f'{self.url}chats/-1/bulk-add/',
            {'user_ids': [1, 2]},
            content_type='application/json',
        )
        self.client.post(
            f'{self.url}chats/-2/bulk-add/',
            {'user_ids': [1, 2]},
            content_type='application/json',
        )
        self.assertEqual(self.user1.chats.count(), 2)
        self.assertEqual(self.user2.chats.count(), 2)

        self.client.post(
            f'{self.url}users/1/bulk-delete/',
            {'chat_ids': [-1, -2]},
            content_type='application/json',
        )
        self.assertEqual(self.user1.chats.count(), 0)
        self.assertEqual(self.user2.chats.count(), 2)

    def test_get_user_admin_chats(self):
        UsersChats.objects.create(
            user=self.user1, chat=self.chat1, is_admin=True
        )
        UsersChats.objects.create(
            user=self.user1, chat=self.chat2, is_admin=False
        )

        rsp = self.client.get(f'{self.url}users/1/admin-chats/')
        self.assertEqual(len(rsp.data), 1)

    def test_get_chat_users(self):
        UsersChats.objects.create(
            user=self.user1, chat=self.chat1, is_admin=True
        )
        UsersChats.objects.create(
            user=self.user2, chat=self.chat1, is_admin=False
        )

        rsp = self.client.get(f'{self.url}chats/-1/users/')
        print(rsp.data)

    def test_update_is_admin(self):
        new_is_admin = True
        UsersChats.objects.create(
            user=self.user1, chat=self.chat1, is_admin=False
        )
        rsp = self.client.patch(
            f'{self.url}chats/-1/update-is-admin/?user_id=1',
            {'is_admin': new_is_admin},
            content_type='application/json',
        )
        self.assertEqual(rsp.data['is_admin'], new_is_admin)

    def test_chats_search(self):
        UsersChats.objects.create(user=self.user1, chat=self.chat1)
        UsersChats.objects.create(user=self.user2, chat=self.chat1)
        rsp = self.client.get(f'{self.url}chats/-1/users/search/?q=u1')
        print(rsp.data)

    def test_users_chats_create(self):
        is_admin1, is_admin2, is_admin3 = False, True, True

        rsp1 = self.client.post(
            f'{self.url}users-chats/',
            {
                'user': self.user1.id,
                'chat': self.chat1.id,
                'is_admin': is_admin1,
            },
        )
        self.assertEqual(rsp1.data['is_admin'], is_admin1)

        rsp2 = self.client.post(
            f'{self.url}users-chats/',
            {
                'user': self.user1.id,
                'chat': self.chat1.id,
                'is_admin': is_admin2,
            },
        )
        self.assertEqual(rsp2.data['is_admin'], is_admin2)

        rsp3 = self.client.post(
            f'{self.url}users-chats/',
            {
                'user': self.user2.id,
                'chat': self.chat1.id,
                'is_admin': is_admin3,
            },
        )
        self.assertEqual(rsp3.data['is_admin'], is_admin3)

        self.assertEqual(rsp1.data['id'], rsp2.data['id'])
        self.assertNotEqual(rsp2.data['id'], rsp3.data['id'])
