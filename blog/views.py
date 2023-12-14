from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Blog, Comment, Post
from blog.permissions import IsAdminUser, IsLoggedIn
from django.views.decorators.csrf import csrf_protect 

from .serializers import (
    BlogSerializer,
    CommentSerializer,
    PostSerializer,
)


class PostApiView(APIView):
    """View class for post model"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsLoggedIn]

    def get(self, request, *args, **kwargs):
        post_data = Post.objects.all()
        serializer = PostSerializer(post_data, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response({"errors": serializer.errors}, status=400)
    
    def put(self, request, pk, format=None):
        instance_data = Post.objects.get(pk=pk)
        serializer = PostSerializer(instance_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(instance_data, data=request.data)
    
    def patch(self, request, pk, format=None):
        instance_data = Post.objects.get(pk=pk)
        serializer = PostSerializer(instance_data, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(instance_data, data=request.data)
    
    def delete(self, request, pk, format=None):
        id = pk
        instance_data = Post.objects.get(pk=id)
        instance_data.delete()
        return Response({'msg':'Message Deleted'})
    

# class CommentApiView(APIView):
#     """View class for comment model"""

#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [IsLoggedIn]

#     def get(self, request, *args, **kwargs):
#         pst = Comment.objects.all()
#         serializer = CommentSerializer(pst, many=True)
#         return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
#         serializer = CommentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         else:
#             return Response({"errors": serializer.errors}, status=400)
        
#     def put(self, request, pk, format=None):
#         id = pk
#         instance_data = Comment.objects.get(pk=id)
#         serializer = CommentSerializer(instance_data, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=200)
#         return Response(instance_data, data=request.data)  
    
#     def patch(self, request, pk, format=None):
#         id = pk
#         instance_data = Comment.objects.get(pk=id)
#         serializer = CommentSerializer(instance_data, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=200)
#         return Response(instance_data, data=request.data)
    
#     def delete(self, request, pk, format=None):
#         id = pk
#         instance_data = Comment.objects.get(id)
#         instance_data.delete()
#         return Response({'msg':'Message Deleted'})  


class BlogVIewSet(viewsets.ModelViewSet):
    """Viwset for blog model"""

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAdminUser]

class CommentViewSet(viewsets.ModelViewSet):
    
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = [IsLoggedIn]