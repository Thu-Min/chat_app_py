import json
import logging

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

logger = logging.getLogger(__name__)

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        try:
            self.chatroom_id = self.scope['url_route']['kwargs'].get('chatroom_id')
            self.room_group_name = f"chatroom_{self.chatroom_id}"
            
            await self.channel_layer.group_add(self.room_group_name, self.channel_name)
            await self.accept()
        except Exception as e:
            logger.error(f"Error during connection: {e}")
            await self.close()

    async def disconnect(self, close_code):
        try:
            await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
        except Exception as e:
            logger.error(f"Error during disconnection: {e}")

    async def receive(self, text_data):
        from .models import Message, User
        from .serializers import MessageSerializer
        
        try:
            data = json.loads(text_data)
            sender = await sync_to_async(User.objects.get)(id=data['sender_id'])
            message = await sync_to_async(Message.objects.create)(
                sender=sender, chatroom_id=self.chatroom_id, content=data['message']
            )
            
            message_data = MessageSerializer(message).data
            
            await self.channel_layer.group_send(
                self.room_group_name,
                {"type": "chat_message", "message": message_data}
            )
        except Exception as e:
            logger.error(f"Error during message receive: {e}")

    async def chat_message(self, event):
        try:
            await self.send(text_data=json.dumps(event["message"]))
        except Exception as e:
            logger.error(f"Error during sending message: {e}")