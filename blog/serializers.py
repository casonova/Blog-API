from blog.models import Post, Creator, Comment, Blog
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "auto_incement_id",
            "title",
            "body",
            "user_type",
            "post_image",
        ]

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
          

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'post',
            'comment_body',
            'user_type',
        ]
        # depth=1
        
    def validate(self, data):
        user_type = data.get('user_type')
        if Creator.objects.filter(user__email = user_type).exists() :
            raise serializers.ValidationError("You are a creator you are not allowed to perform this action. ")
        return data
    

class BlogSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True)
    comments = CommentSerializer(many=True)
    class Meta:
        model = Blog
        fields = ['id',"name", "posts","comments"]
        
    def create(self, validated_data):
        user = self.context.get("request").user
        if user.is_superuser:
            post_data  = validated_data.pop('posts')
            comment_data = validated_data.pop('comments')
            if post_data or comment_data :
                blog_instance = Blog.objects.create(**validated_data)
                for post_data in post_data:
                    Post.objects.create(blog=blog_instance, **post_data)
                for comment_data in comment_data:
                    Comment.objects.create(blog=blog_instance, **comment_data)
                        
                return blog_instance 
        
        else:
            raise serializers.ValidationError("You must be an admin to perform this action.")  
    
    def update(self, instance, validated_data):
        user = self.context.get("request").user
        print(user)
        
        if user.is_superuser:
            instance.name = validated_data.get('name', instance.name)
            instance.save()
            posts_data = validated_data.get('posts', instance.posts)
            post_detail = (instance.posts).all()
            post_detail = list(post_detail)

            comments_data = validated_data.get("comments",instance.comments)
            comments_detail = (instance.comments).all()
            comments_detail =list(comments_detail)
            
            for post_data in posts_data:
                posts_instance= post_detail.pop(0)
                posts_instance.title = post_data.get('title')
                posts_instance.body = post_data.get('body')
                posts_instance.post_image = post_data.get('post_image')
                posts_instance.user_type = post_data.get('user_type')
                posts_instance.save()
                
            for comment_data in comments_data:   
                comment_instance = comments_detail.pop(0)
                comment_instance.comment_body = comment_data.get('comment_body')
                comment_instance.save()
                    
                return instance
        
        else:
            raise serializers.ValidationError("You must be an admin to perform this action.")

 