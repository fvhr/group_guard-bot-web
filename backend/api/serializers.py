from rest_framework.serializers import ModelSerializer

from . import models


class UserSerializer(ModelSerializer):
    class Meta:
        model = models.User
        exclude = ('groups', 'user_permissions', 'last_login', 'is_superuser', 'is_active')
        extra_kwargs = {
            'password': {'write_only': True},
            'is_staff': {'read_only': True},
            'date_joined': {'read_only': True},
        }


class ChatSerializer(ModelSerializer):
    class Meta:
        model = models.Chat
        fields = '__all__'


class UsersChatsSerializer(ModelSerializer):
    class Meta:
        model = models.UsersChats
        fields = '__all__'


class PhoneSerializer(ModelSerializer):
    class Meta:
        model = models.Phone
        fields = '__all__'
