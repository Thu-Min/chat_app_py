from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from chat.models import Message, Chat_Room_Member, Chat_Room, User
from chat.serializers import MessageSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def message_list(request):
    messages = Message.objects.all().order_by('-timestamp')[:10]
    serializer = MessageSerializer(messages, many=True)
    
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_chat_room(request):
    type = request.data.get('type')
    members = request.data.get('members')

    chat_room, created = Chat_Room.objects.get_or_create(type=type)
    if created:
        chat_room.save()

    Chat_Room_Member.objects.get_or_create(chatroom=chat_room, user=request.user, role='admin')

    for member in members:
        user = User.objects.get(id=member['id'])
        Chat_Room_Member.objects.get_or_create(chatroom=chat_room, user=user, role='member')

    return Response({'chat_room': chat_room.id})

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def send_message(request):