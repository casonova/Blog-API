from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import User


class Blog(models.Model):
    """Model for Blog"""

    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    """Model for Post"""

    auto_incement_id = models.AutoField(primary_key=True)
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, null=True, blank=True, related_name="posts"
    )
    title = models.CharField(max_length=15)
    body = models.TextField()
    user_type = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post_image = models.ImageField(upload_to="media", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["auto_incement_id"]

    @property
    def comments_count(self):
        return self.comments.count()


class Comment(models.Model):
    """Model for Comment"""

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, null=True, blank=True, related_name="comments"
    )
    user_type = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at", "-updated_at"]
