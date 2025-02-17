from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("The Username field must be set")
        
        user = self.model(username=username)
        user.set_password(password)
        
        user.save(using=self._db)
        
        return user
    
class User(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'
    
    objects = UserManager()
    
    def __str__(self):
        return self.username
    
class Chat_Room(models.Model):
    type = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.type
    
class Chat_Room_Member(models.Model):
    chatroom_id = models.ForeignKey(Chat_Room, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.chatroom_id.type}: {self.user_id.username}"

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.sender.username}: {self.content}"