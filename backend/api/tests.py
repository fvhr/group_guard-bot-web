from django.test import TestCase
from .models import User, Chat, UsersChats


class APITestCase(TestCase):
    def setUp(self) -> None:
        self.url = 'http://localhost/api/'

        self.user1 = User.objects.create_user('u1', None, 'u1', id=1)
        self.user2 = User.objects.create_user('u2', None, 'u2', id=2)

        self.chat1 = Chat.objects.create(id=-1, title='c1')
        self.chat2 = Chat.objects.create(id=-2, title='c2')

    def test_user_create(self):
        rsp = self.client.post(f'{self.url}users/', {'id': 3})
        print(rsp.data)

    def test_users_chats_bulk_create_and_delete(self):
        self.assertEqual(self.user1.chats.count(), 0)

        rsp = self.client.post(
            f'{self.url}chats/-1/bulk-add/',
            {'user_ids': [1, 2]},
            content_type='application/json'
        )
        rsp = self.client.post(
            f'{self.url}chats/-2/bulk-add/',
            {'user_ids': [1, 2]},
            content_type='application/json'
        )
        self.assertEqual(self.user1.chats.count(), 2)
        self.assertEqual(self.user2.chats.count(), 2)

        rsp = self.client.post(
            f'{self.url}users/1/bulk-delete/',
            {'chat_ids': [-1, -2]},
            content_type='application/json'
        )
        self.assertEqual(self.user1.chats.count(), 0)
        self.assertEqual(self.user2.chats.count(), 2)
