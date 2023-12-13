from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Blog, Comment, Creator, Post
from blog.permissions import IsAdminUser, IsLoggedIn
from django.views.decorators.csrf import csrf_protect 

from .serializers import (
    BlogSerializer,
    CommentSerializer,
    CreatorSerializer,
    PostSerializer,
)


class PostApiView(APIView):
    """View class for post model"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsLoggedIn]

    @csrf_protect 
    def get(self, request, *args, **kwargs):
        pst = Post.objects.all()
        serializer = PostSerializer(pst, many=True)
        return Response(serializer.data)

    @csrf_protect 
    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response({"errors": serializer.errors}, status=400)


class CommentApiView(APIView):
    """View class for comment model"""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]

    @csrf_protect 
    def get(self, request, *args, **kwargs):
        pst = Comment.objects.all()
        serializer = CommentSerializer(pst, many=True)
        return Response(serializer.data)

    @csrf_protect 
    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response({"errors": serializer.errors}, status=400)


class BlogVIewSet(viewsets.ModelViewSet):
    """Viwset for blog model"""

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAdminUser]
