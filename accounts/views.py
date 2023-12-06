from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
)
from .serializers import UserSerializer
from accounts.models import User


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    
class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer    