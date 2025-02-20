from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from chat.models import User
from chat.serializers import UserSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_users(request):
    users = User.objects.exclude(id=request.user.id)
    serializer = UserSerializer(users, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def online_users(request):
    users = User.objects.filter(is_active=True).exclude(id=request.user.id)
    serializer = UserSerializer(users, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def offline_users(request):
    users = User.objects.filter(is_active=False)
    serializer = UserSerializer(users, many=True)
    
    return Response(serializer.data)
