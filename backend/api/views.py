from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from . import models, serializers


class UserViewSet(ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

    @action(['GET'], True, 'admin-chats', 'user-admin-chats')
    def admin_chats(self, request: Request, pk: int):
        try:
            pk = int(pk)
        except ValueError:
            return Response({'detail': 'user does not exists'}, 404)

        chats = list(models.Chat.objects.filter(admins__contains=[int(pk)]).values_list('id', flat=True))
        return Response({'chats': chats}, 200)


class ChatViewSet(ModelViewSet):
    queryset = models.Chat.objects.all()
    serializer_class = serializers.ChatSerializer


class UsersChatsViewSet(ModelViewSet):
    queryset = models.UsersChats.objects.all()
    serializer_class = serializers.UsersChatsSerializer


class PhoneViewSet(ModelViewSet):
    queryset = models.Phone.objects.all()
    serializer_class = serializers.PhoneSerializer

    @swagger_auto_schema('GET', manual_parameters=[
        openapi.Parameter(
            'number', openapi.IN_QUERY, 'phone number to check its existence', True, type=openapi.TYPE_STRING
        ),
    ])
    @action(['GET'], False, 'exists', 'phone-exists')
    def phone_exists(self, request: Request):
        number = request.query_params.get('number', None)
        if models.Phone.objects.filter(number=number):
            return Response({'exists': True}, 200)
        return Response({'exists': False}, 404)
