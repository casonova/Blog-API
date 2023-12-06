from rest_framework.response import Response
from rest_framework.views import APIView
from blog.models import Post, Comment, Blog
from .serializers import PostListCreateSerializer, CommentListCreateSerializer, BlogSerializer
from rest_framework import viewsets
# from rest_framework import status


class ListCreatePostAPIView(APIView):
    queryset = Post.objects.all()
    serializer_class = PostListCreateSerializer

    def get(self, request, *args, **kwargs):
        stu = Post.objects.all()
        serializer = PostListCreateSerializer(stu, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = PostListCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response({"errors": serializer.errors}, status=400)
        

class ListCreateCommentAPIView(APIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListCreateSerializer

    def get(self, request, *args, **kwargs):
        stu = Comment.objects.all()
        serializer = CommentListCreateSerializer(stu, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = CommentListCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response({"errors": serializer.errors}, status=400)        

class BlogVIewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer