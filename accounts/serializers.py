from rest_framework import serializers

from .models import User

from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model"""

    class Meta:
        model = User
        fields = ["id", "username", "name", "email", "password", "action_choice"]


# class LoginSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = User
#         fields = ["id", "email", "password"]

class UserLoginSerializer(serializers.Serializer):
    """
    Serializer class to authenticate users with email and password.
    """

    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        print(user)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")