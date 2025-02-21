from datetime import timedelta
from django.contrib.auth import login
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from chat.models import User
from chat.serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
def user_login(request):
    try:
        username = request.data.get('username')
        
        if not username:
            return Response({
                'error': "Username is required."
            }, status=status.HTTP_400_BAD_REQUEST)
                
        user, created = User.objects.get_or_create(username=username)
        login(request, user)
        user.is_active = True
        user.save()
        
        refresh = RefreshToken.for_user(user)
        refresh.set_exp(lifetime=timedelta(days=7))  # Set token lifetime to 7 days
        
        return Response({
            'user': UserSerializer(user).data,
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        })
    except Exception as e:
        return Response({
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    try:
        refresh_token = request.data.get("refresh_token")
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({"message": "Logged out successfully"})
    except Exception as e:
        return Response({"error": "Invalid token"}, status=400)