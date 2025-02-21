from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import auth_views, message_views, chat_views, user_views

urlpatterns = [
    # Auth APIs
    path('api/login/', auth_views.user_login, name='login'),
    path('api/logout/', auth_views.user_logout, name='logout'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Chat APIs 
    path('api/create_chat_room/', chat_views.create_chat_room, name='create_chat_room'),
    path('api/chat_rooms/', chat_views.chat_room_list, name='chat_room_list'),
    path('api/chat_room/', chat_views.get_chat_room, name='chat_room'),
    path('api/delete_chat_room/', chat_views.delete_chat_room, name='delete_chat_room'),
    path('api/add_member/', chat_views.add_member_to_chat, name="add_member"),
    
    # Message APIs
    path('api/messages/', message_views.message_list_by_chat_room, name='message_list'),
    path('api/send_message/', message_views.send_message, name='send_message'),
    
    # User APIs
    path('api/online_users/', user_views.online_users, name='online_users'),
    path('api/offline_users/', user_views.offline_users, name='offline_users'),
    path('api/users/', user_views.all_users, name='all_users'),
]
