from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('users', views.UserViewSet, 'users')
router.register('chats', views.ChatViewSet, 'chat')
router.register('users-chats', views.UsersChatsViewSet, 'users-chats')

urlpatterns = [path('', include(router.urls))]
