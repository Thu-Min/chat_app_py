from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from chat.models import Chat_Room_Member, Chat_Room, User, Message
from chat.serializers import ChatRoomSerializer
from django.utils.timesince import timesince

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_chat_room(request):
    try:
        chatroom_id = request.query_params.get('chatroom_id')
        chatroom = Chat_Room.objects.get(id=chatroom_id)

        members = Chat_Room_Member.objects.filter(chatroom=chatroom).exclude(user=request.user)
        members_data = [{'id': member.user.id, 'username': member.user.username} for member in members]
        
        chat_room_data = ChatRoomSerializer(chatroom).data
        chat_room_data['members'] = members_data
        
        return Response(chat_room_data)
    except Chat_Room.DoesNotExist:
        return Response({'error': 'Chat room not found.'}, status=404)
    except Exception as e:
        return Response({'error': str(e)}, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_chat_room(request):
    try:
        type = request.data.get('type')
        members = request.data.get('members')

        chat_room = Chat_Room.objects.create(type=type)
        chat_room.save()

        Chat_Room_Member.objects.get_or_create(chatroom=chat_room, user=request.user, role='admin')

        members_data = []
        for member in members:
            user = User.objects.get(id=member['id'])
            Chat_Room_Member.objects.get_or_create(chatroom=chat_room, user=user, role='member')
            members_data.append({'id': user.id, 'username': user.username})

        chat_room_data = ChatRoomSerializer(chat_room).data
        chat_room_data['members'] = members_data
        chat_room_data['last_message'] = None

        return Response(chat_room_data)
    except Exception as e:
        return Response({'error': str(e)}, status=400)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def chat_room_list(request):
    try:
        chat_room_members = Chat_Room_Member.objects.filter(user=request.user)
        chat_rooms = [member.chatroom for member in chat_room_members]
        
        chat_rooms_data = []
        for chat_room in chat_rooms:
            members = Chat_Room_Member.objects.filter(chatroom=chat_room).exclude(user=request.user)
            members_data = [{'id': member.user.id, 'username': member.user.username} for member in members]
            
            last_message = Message.objects.filter(chatroom=chat_room).order_by('-timestamp').first()
            if last_message:
                time_since = timesince(last_message.timestamp)
                
                if 'minute' in time_since:
                    time_since = time_since.split(',')[0]
                elif 'hour' in time_since:
                    time_since = time_since.split(',')[0]
                
                last_message_data = {
                    'content': last_message.content,
                    'sent_time': time_since + ' ago'
                }
            else:
                last_message_data = None
                
            chat_room_data = ChatRoomSerializer(chat_room).data
            chat_room_data['members'] = members_data
            chat_room_data['last_message'] = last_message_data
            chat_rooms_data.append(chat_room_data)
        
        return Response(chat_rooms_data)
    except Exception as e:
        return Response({'error': str(e)}, status=400)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_chat_room(request):
    try:
        chatroom_id = request.data.get('chatroom_id')
        chatroom = Chat_Room.objects.get(id=chatroom_id)

        Chat_Room_Member.objects.filter(chatroom=chatroom).delete()

        Message.objects.filter(chatroom=chatroom).delete()

        chatroom.delete()
        return Response({'success': 'Chat room and its related data deleted successfully.'})
    except Chat_Room.DoesNotExist:
        return Response({'error': 'Chat room not found.'}, status=404)
    except Exception as e:
        return Response({'error': str(e)}, status=400)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_member_to_chat(request):
    try:
        chatroom_id = request.data.get('chatroom_id')
        user_id = request.data.get('user_id')

        chatroom = Chat_Room.objects.get(id=chatroom_id)
        user = User.objects.get(id=user_id)

        if chatroom.type == 'private':
            chatroom.type = 'group'
            chatroom.save()

        Chat_Room_Member.objects.get_or_create(chatroom=chatroom, user=user, role='member')

        members = Chat_Room_Member.objects.filter(chatroom=chatroom).exclude(user=request.user)
        members_data = [{'id': member.user.id, 'username': member.user.username} for member in members]

        chat_room_data = ChatRoomSerializer(chatroom).data
        chat_room_data['members'] = members_data

        return Response(chat_room_data)
    except Chat_Room.DoesNotExist:
        return Response({'error': 'Chat room not found.'}, status=404)
    except User.DoesNotExist:
        return Response({'error': 'User not found.'}, status=404)
    except Exception as e:
        return Response({'error': str(e)}, status=400)