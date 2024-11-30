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

    @swagger_auto_schema('GET', responses={
        200: serializers.ChatSerializer(many=True),
    })
    @action(['GET'], True, 'admin-chats', 'user-admin-chats')
    def admin_chats(self, request: Request, pk: int):
        try:
            pk = int(pk)
        except ValueError:
            return Response({'detail': 'user does not exists'}, 404)

        chats = list(models.UsersChats.objects.filter(user_id=pk, is_admin=True).values_list('chat_id', flat=True))
        return Response(chats, 200)

    @swagger_auto_schema('POST', request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'chat_ids': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.TYPE_INTEGER)
        }
    ))
    @action(['POST'], True, 'bulk-delete', 'user-bulk-delete')
    def bulk_delete(self, request: Request, pk):
        chats_ids = request.data.get('chat_ids', [])
        user = self.get_object()
        models.UsersChats.objects.filter(user=user, chat__in=chats_ids).delete()
        return Response(status=204)


class ChatViewSet(ModelViewSet):
    queryset = models.Chat.objects.all()
    serializer_class = serializers.ChatSerializer

    @action(['GET'], True, 'users', 'chat-users')
    def users(self, request: Request, pk: int):
        users = models.User.objects.filter(chats__chat_id=pk)
        users = serializers.UserSerializer(instance=users, many=True).data
        return Response(users, 200)

    @swagger_auto_schema('POST', request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'user_ids': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.TYPE_INTEGER)
        }
    ), responses={
        200: openapi.Response('success', serializers.UsersChatsSerializer(many=True))
    })
    @action(['POST'], True, 'bulk-add', 'users-chats-bulk-add')
    def bulk_create(self, request: Request, pk: int):
        user_ids = request.data.get('user_ids', [])
        chat = self.get_object()
        users_chats = models.UsersChats.objects.bulk_create([
            models.UsersChats(user_id=user_id, chat=chat) for user_id in user_ids
        ])
        data = serializers.UsersChatsSerializer(instance=users_chats, many=True).data
        return Response(data, 200)


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
    ], responses={
        200: '{"exists": True}',
        404: '{"exists": False}',
    })
    @action(['GET'], False, 'exists', 'phone-exists')
    def phone_exists(self, request: Request):
        number = request.query_params.get('number', None)
        if models.Phone.objects.filter(number=number):
            return Response({'exists': True}, 200)
        return Response({'exists': False}, 404)
