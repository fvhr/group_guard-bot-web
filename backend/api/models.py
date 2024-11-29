from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = models.BigAutoField(primary_key=True)


class Chat(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    url = models.CharField(max_length=255, null=True)
    avatar_url = models.CharField(max_length=255, null=True)
    admins = models.JSONField(null=True)
    bot_is_admin = models.BooleanField(default=False)
    objects: models.Manager

    def __str__(self):
        return self.title


class UsersChats(models.Model):
    user_id = models.ForeignKey(User, models.CASCADE, 'chats')
    chat_id = models.ForeignKey(Chat, models.CASCADE, 'users')
    objects: models.Manager


class Phone(models.Model):
    number = models.CharField(max_length=20)
    objects: models.Manager

    def __str__(self):
        return self.number
