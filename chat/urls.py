from django.urls import path
from .views import auth_views, message_views, user_views

urlpatterns = [
    # Auth APIs
    path('api/login/', auth_views.user_login, name='login'),
    path('api/logout/', auth_views.user_logout, name='logout'),
    
    # Chat APIs 
    path('api/messages/', message_views.message_list, name='message_list'),
    path('api/create_chat_room/', message_views.create_chat_room, name='create_chat_room'),
    
    # User APIs
    path('api/online/', user_views.online_users, name='online_users'),
]
