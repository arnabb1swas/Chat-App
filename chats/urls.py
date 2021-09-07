from django.urls import path
from . import views
from django.contrib.auth import logout

urlpatterns = [
    # index page url
    path('', views.index, name='index'),

    # user's all chats list url
    path('chat/', views.chatList, name='chats'),

    # user's chats url
    path('chat/<int:sender>/<int:receiver>/',
         views.messageDetail, name='chat'),

    # api's for user chats url
    path('api/messages/<int:sender>/<int:receiver>/', views.messageList,
         name='message-detail'),

    # api's for user chat list url
    path('api/messages/', views.messageList, name='message-list'),

    # directly logout user using auth  url
    path('logout/', views.logout_view, name='logout'),

    # register's the user url
    path('register/', views.register_view,
         name='register'),
]
