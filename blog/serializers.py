# from accounts.models import User
from blog.models import Post, Creator, Comment, Blog
from rest_framework import serializers
# import oszd
# from django.conf import settings


class PostListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "body",
            "user_type",
            "post_image",
        ]
    
    def get_comments_count(self, obj):
        return obj.comments_count
    
    def validate(self, data):
        user_type = data.get('user_type')
        if not Creator.objects.filter(user__email = user_type).exists() :
            raise serializers.ValidationError("You are not allowed to perform this action, First make yourself creator")
        return data
    
    def validate_title(self, value):
        if len(value) > 15:
            raise serializers.ValidationError("Max title length is 15 characters")
        return value

    def validate_body(self, value):
        if len(value) > 200:
            raise serializers.ValidationError("Max body length is 200 characters")
        return value
    

class CommentListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'post',
            'comment_body',
            'user_type'
        ]
    
    def validate(self, data):
        user_type = data.get('user_type')
        if  Creator.objects.filter(user__email = user_type).exists() :
            raise serializers.ValidationError("You are not allowed to perform this action, Only visitor can perform this")
        return data
    
    def validate_comment_body(self, value):
        if len(value) > 100:
            raise serializers.ValidationError("Max comment_body length is 100 characters")
        return value
    

class BlogSerializer(serializers.ModelSerializer):
    post_field = PostListCreateSerializer(many=True, required=False) 

    class Meta:
        model = Blog
        fields = ['post_field']
        
    def create(self, validated_data):
        posts_data = validated_data.pop('post_field', None)
        blog_instance = Blog.objects.create(**validated_data)

        if posts_data:
            for post_data in posts_data:
                post_serializer = PostListCreateSerializer(data=post_data)
                if post_serializer.is_valid():
                    post_serializer.save(blog=blog_instance) 

        return blog_instance

    def update(self, instance, validated_data):
        posts_data = validated_data.pop('post_field', None)
        instance = super().update(instance, validated_data)

        if posts_data:
            for post_data in posts_data:
                post_instance = instance.post 
                post_instance.title = post_data.get('title', post_instance.title)
                post_instance.body = post_data.get('body', post_instance.body)
                post_instance.post_image = post_data.get('post_image', post_instance.post_image)
                post_instance.save()

        return instance


          
                