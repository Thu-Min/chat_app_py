from django.urls import path
from .views import auth_views, message_views, chat_views, user_views

urlpatterns = [
    # Auth APIs
    path('api/login/', auth_views.user_login, name='login'),
    path('api/logout/', auth_views.user_logout, name='logout'),
    
    # Chat APIs 
    path('api/create_chat_room/', chat_views.create_chat_room, name='create_chat_room'),
    path('api/chat_rooms/', chat_views.chat_room_list, name='chat_room_list'),
    
    # Message APIs
    path('api/messages/', message_views.message_list_by_chat_room, name='message_list'),
    path('api/send_message/', message_views.send_message, name='send_message'),
    
    # User APIs
    path('api/online/', user_views.online_users, name='online_users'),
    path('api/users/', user_views.all_users, name='all_users'),
]
