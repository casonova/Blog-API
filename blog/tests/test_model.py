from django.test import TestCase
from blog.models import Blog, Post, Comment
from accounts.models import User
from accounts.models import CustomUserManager
from django.test import TestCase


class CustomUserManagerTestCase(TestCase):
    def test_create_user(self):

        manager = User.objects
        user = manager.create_user(email="test@example.com", password="password123")

        self.assertEqual(user.email, "test@example.com")
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        
        manager = User.objects
        superuser = manager.create_superuser(email="admin@example.com", password="admin123")

        self.assertEqual(superuser.email, "admin@example.com")
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)


class UserModelTestCase(TestCase):
    def test_user_creation(self):

        user = User.objects.create(
            email="test@example.com",
            username="testuser",
            password="password123",
            action_choice="visitor"
        )

        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.username, "testuser")
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.is_active)


    def test_admin_user_creation(self):

        admin_user = User.objects.create(
            email="admin@example.com",
            username="adminuser",
            password="admin123",
            action_choice="admin"
        )

        self.assertEqual(admin_user.email, "admin@example.com")
        self.assertEqual(admin_user.username, "adminuser")
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        self.assertTrue(admin_user.is_active)
           

class BlogModelTestCase(TestCase):
    def setUp(self):
        self.blog = Blog.objects.create(name="Blog 1")
    
    def test_blog_creation(self):
        self.assertEqual(self.blog.name, "Blog 1")    
      
           
class PostModelTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(
                email="zainab@gmail.com",
                username="zainab",
                name="zainab",
                password="zainab"
            )
        self.blog = Blog.objects.create(name="Blog 1")
        self.post = Post.objects.create(
                blog=self.blog,
                title="Sicology",
                body="Sicology",
                user_type=self.user1
            )
    
    def test_post_creation(self):
        self.assertEqual(self.post.title, "Sicology")   
     
        
class CommentModelTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(
                email="zainab@gmail.com",
                username="zainab",
                name="zainab",
                password="zainab"
            )
        self.blog = Blog.objects.create(name="Blog 1")
        self.post = Post.objects.create(
                blog=self.blog,
                title="Sicology",
                body="Sicology",
                user_type=self.user1
            )
        self.comment = Comment.objects.create(
                post = self.post, 
                blog=self.blog, 
                user_type=self.user1, 
                comment_body="body"
            )
    
    def test_post_creation(self):
        self.assertEqual(self.comment.post.title, "Sicology") 
        self.assertEqual(self.comment.blog.name, "Blog 1") 
        self.assertEqual(self.comment.comment_body, "body") 
