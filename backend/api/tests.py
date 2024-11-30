from django.test import TestCase
from .models import User, Chat, UsersChats


class APITestCase(TestCase):
    def setUp(self) -> None:
        self.url = 'http://localhost/api/'
        self.user1 = User.objects.create_user('u1', None, 'u1', id=1)
        self.chat1 = Chat.objects.create(id=-1, title='c1')
        self.chat2 = Chat.objects.create(id=-2, title='c2')

        # UsersChats.objects.create(user=self.user1, chat=self.chat1)

    def test_user_chats_bulk_create(self):
        rsp = self.client.post(
            f'{self.url}chats/-2/bulk-add/',
            {'user_ids': [1]},
            content_type='application/json'
        )
        print(rsp.data)
        return self.assertEqual(self.user1.chats.count(), 1)

    def test_user_chats_bulk_delete(self):
        rsp = self.client.post(
            f'{self.url}users/1/bulk-delete/',
            {'chat_ids': [-1, 2]},
            content_type='application/json'
        )
        return self.assertEqual(self.user1.chats.count(), 0)
