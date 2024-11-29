from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    tg_id = models.BigIntegerField()


class Chat(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    url = models.CharField(max_length=255)
    objects: models.Manager

    def __str__(self):
        return self.name


class UsersChats(models.Model):
    user_id = models.ForeignKey(User, models.CASCADE, 'chats')
    chat_id = models.ForeignKey(Chat, models.CASCADE, 'users')
    objects: models.Manager


class Phone(models.Model):
    number = models.CharField(max_length=20)
    objects: models.Manager

    def __str__(self):
        return self.number
