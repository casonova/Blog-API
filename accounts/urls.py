from django.urls import path

from .views import UserCreateAPIView, UserListAPIView, LoginAPIView, UserLogoutAPIView

urlpatterns = [
    path("", UserListAPIView.as_view(), name="user_detail"),
    path("register/", UserCreateAPIView.as_view(), name="user_create"),
    path("login/",LoginAPIView.as_view(), name="login"),
    path('logout/', UserLogoutAPIView.as_view(), name="logout")
]
