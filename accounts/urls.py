from django.urls import path
from .views import UserCreateAPIView, UserListAPIView

urlpatterns = [
    path("", UserListAPIView.as_view(), name="user_detail"),
    path("register/", UserCreateAPIView.as_view(), name="user_create"),
]