from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Blog, Comment, Post

from .serializers import BlogSerializer, CommentSerializer, PostSerializer


class PostApiView(APIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        pst = Post.objects.all()
        serializer = PostSerializer(pst, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response({"errors": serializer.errors}, status=400)


class CommentApiView(APIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get(self, request, *args, **kwargs):
        pst = Comment.objects.all()
        serializer = CommentSerializer(pst, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response({"errors": serializer.errors}, status=400)


class BlogVIewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
