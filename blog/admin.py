from django.contrib import admin
from blog.models import Post, Creator, Comment, Blog


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','body','user_type','created_at','updated_at','post_image']
    search_fields = ['user']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post','user_type','comment_body','created_at','updated_at']

    
@admin.register(Creator)
class CreatorAdmin(admin.ModelAdmin):
    list_display = ['user']      
    

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display =['post']
    