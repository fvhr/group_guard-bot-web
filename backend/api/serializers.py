from rest_framework.serializers import ModelSerializer

from . import models, utils


class UserSerializer(ModelSerializer):
    class Meta:
        model = models.User
        exclude = (
            'groups', 'user_permissions', 'last_login',
            'is_active', 'is_staff', 'is_superuser', 'password',
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


class UsersChatsWithUserSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = models.UsersChats
        fields = ('user', 'is_admin')


class PhoneSerializer(ModelSerializer):
    class Meta:
        model = models.Phone
        fields = '__all__'
