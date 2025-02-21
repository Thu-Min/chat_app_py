from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from chat.models import Message, Chat_Room
from chat.serializers import MessageSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def message_list_by_chat_room(request):
    try:
        chatroom_id = request.query_params.get('chatroom_id')
        messages = Message.objects.filter(chatroom=chatroom_id).order_by('id')
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_message(request):
    try:
        chatroom_id = request.data.get('chatroom_id')
        content = request.data.get('content')
        
        chatroom = Chat_Room.objects.get(id=chatroom_id)
        message = Message(sender=request.user, content=content, chatroom=chatroom)
        message.save()
        
        serializer = MessageSerializer(message)
        return Response(serializer.data)
    except Chat_Room.DoesNotExist:
        return Response({'error': 'Chat room not found'}, status=404)
    except Exception as e:
        return Response({'error': str(e)}, status=400)