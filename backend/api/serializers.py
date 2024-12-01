from rest_framework.serializers import ModelSerializer

from . import models, utils


class UserSerializer(ModelSerializer):
    class Meta:
        model = models.User
        exclude = (
            'groups',
            'user_permissions',
            'last_login',
            'is_active',
            'is_superuser',
            'password',
        )
        extra_kwargs = {
            'date_joined': {'read_only': True},
        }

    def create(self, validated_data: dict):
        validated_data['password'] = utils.generate_password()
        return models.User.objects.create_user(
            validated_data.pop('username', ' '),
            validated_data.pop('email', None),
            validated_data.pop('password', None),
            **validated_data
        )


class ChatSerializer(ModelSerializer):
    class Meta:
        model = models.Chat
        fields = '__all__'


class UsersChatsSerializer(ModelSerializer):
    class Meta:
        model = models.UsersChats
        fields = '__all__'

    def create(self, validated_data: dict):
        is_admin = validated_data.pop('is_admin', False)
        try:
            obj = models.UsersChats.objects.get(**validated_data)
            obj.is_admin = is_admin
            obj.save()
            return obj
        except models.UsersChats.DoesNotExist:
            validated_data.setdefault('is_admin', is_admin)
            return models.UsersChats.objects.create(**validated_data)


class UsersChatsWithUserSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = models.UsersChats
        fields = ('user', 'is_admin')
