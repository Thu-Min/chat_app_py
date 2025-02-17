from rest_framework import serializers
from .models import User, Message, Chat_Room, Chat_Room_Member

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'is_active']
        
class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    
    class Meta:
        model = Message
        fields = ['id', 'sender', 'content', 'timestamp']
        
class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat_Room
        fields = ['id', 'type', 'timestamp']
        
class ChatRoomMemberSerializer(serializers.ModelSerializer):
    chatroom_id = ChatRoomSerializer(read_only=True)
    user_id = UserSerializer(read_only=True)
    
    class Meta:
        model = Chat_Room_Member
        fields = ['id', 'chatroom_id', 'user_id', 'role', 'timestamp']