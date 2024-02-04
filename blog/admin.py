from django.contrib import admin

from blog.models import Blog, Comment, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "auto_incement_id",
        "blog",
        "title",
        "body",
        "user_type",
        "created_at",
        "updated_at",
        "post_image",
    ]
    search_fields = ["blog"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["id", "post", "user_type", "comment_body", "created_at", "updated_at"]


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
