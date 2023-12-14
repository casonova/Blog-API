from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from accounts.models import User

from .serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    """View to create a user"""
    
    serializer_class = UserSerializer


class UserListAPIView(ListAPIView):
    """View to get all user"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
