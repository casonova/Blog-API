from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, ListAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_205_RESET_CONTENT, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.models import User
from blog.permissions import IsAdminUser, IsLoggedIn
from .serializers import UserSerializer, UserLoginSerializer


class UserCreateAPIView(CreateAPIView):
    """View to create a user"""
    
    serializer_class = UserSerializer


class UserListAPIView(ListAPIView):
    """View to get all user"""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginAPIView(APIView):

    def post(self, request):
        
        serializer = UserLoginSerializer(data=request.data)
        
        if serializer.is_valid():
            email = serializer.data.get('email')
            password = serializer.data.get('password')

            if email is None or password is None:
                return Response({'error': 'Please provide both email and password'}, status=HTTP_400_BAD_REQUEST)

            if not User.objects.filter(email=email).exists():
                return Response({'error': 'Invalid Credentials'}, status=HTTP_401_UNAUTHORIZED)
            
            user = User.objects.get(email=email)

            refresh = RefreshToken.for_user(user)
            token = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response(token, status=HTTP_200_OK)
        return Response({"errors": serializer.errors}, status=400)
    
    
class UserLogoutAPIView(APIView):
    permission_classes = [IsLoggedIn]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"success": "User successfully logged out"}, status=HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": "Invalid token or token not provided"}, status=HTTP_401_UNAUTHORIZED)