from django.urls import path
from .views import user_login, user_logout, message_list, online_users

urlpatterns = [
    path('api/login/', user_login, name='login'),
    path('api/logout/', user_logout, name='logout'),
    path('api/messages/', message_list, name='message_list'),
    path('api/online/', online_users, name='online_users'),
]
