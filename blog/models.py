from django.db import models
from accounts.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Creator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.email
       

class Post(models.Model):
    title = models.CharField(max_length=15, unique=True)
    body = models.TextField()
    user_type =  models.ForeignKey(User,on_delete=models.CASCADE)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post_image = models.ImageField(upload_to='media', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["id"]

    @property
    def comments_count(self):
        return self.comments.count()


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user_type =  models.ForeignKey(User,on_delete=models.CASCADE)  
    comment_body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at", "-updated_at"]
        
                

class Blog(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='post')
    # comment = models.ForeignKey(Comment,on_delete=models.CASCADE)

    def __str__(self):
        return f"Blog for {self.post.title}"

    # @receiver(post_save, sender=Post)
    # @receiver(post_save, sender=Comment)
    # def update_blog_info(sender, instance, created, **kwargs):
    #     if sender == Post:
    #         blog, created = Blog.objects.get_or_create(post=instance)
    #         blog.post_title = instance.title
    #         blog.comments_count = instance.comment_set.count()
    #         blog.save()
    #     elif sender == Comment:
    #         post = instance.post
    #         blog, created = Blog.objects.get_or_create(post=post)
    #         blog.comments_count = post.comment_set.count()
    #         blog.save()     
            
            
  
        