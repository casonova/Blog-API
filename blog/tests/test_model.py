# from rest_framework.test import APITestCase
# from django.urls import reverse
# from blog.models import Blog, Creator, Post, Comment
# from accounts.models import User
# from rest_framework.test import APIRequestFactory
# from blog.views import *
# from accounts.views import UserListAPIView
# from rest_framework.test import APIClient

# class UserModelTestCase(APITestCase):
#     def setUp(self):
#         self.user = User.objects.create(
#             email="ali@gmail.com",
#             username="ali",
#             name="ali",
#             password="ali",
#         )
        
#     def test_user_creation(self):
#         self.assertEqual(self.user.email, "ali@gmail.com")
#         self.assertTrue(self.user.check_password("ali")) 
        

# class BLogModelTestCase(APITestCase):
#     def setUp(self):
#         self.blog = Blog.objects.create(name="Blog 1")
    
#     def test_blog_creation(self):
#         self.assertEqual(self.blog.name, "Blog 1")    
      
           
# class PostModelTestCase(APITestCase):
#     def setUp(self):
#         self.user1 = User.objects.create(
#                 email="zainab@gmail.com",
#                 username="zainab",
#                 name="zainab",
#                 password="zainab"
#             )
#         self.blog = Blog.objects.create(name="Blog 1")
#         self.post = Post.objects.create(
#                 blog=self.blog,
#                 title="Sicology",
#                 body="Sicology",
#                 user_type=self.user1
#             )
    
#     def test_post_creation(self):
#         self.assertEqual(self.post.title, "Sicology")   
     
        
# class CommentModelTestCase(APITestCase):
#     def setUp(self):
#         self.user1 = User.objects.create(
#                 email="zainab@gmail.com",
#                 username="zainab",
#                 name="zainab",
#                 password="zainab"
#             )
#         self.blog = Blog.objects.create(name="Blog 1")
#         self.post = Post.objects.create(
#                 blog=self.blog,
#                 title="Sicology",
#                 body="Sicology",
#                 user_type=self.user1
#             )
#         self.comment = Comment.objects.create(
#                 post = self.post, 
#                 blog=self.blog, 
#                 user_type=self.user1, 
#                 comment_body="body"
#             )
    
#     def test_post_creation(self):
#         self.assertEqual(self.comment.post.title, "Sicology") 
#         self.assertEqual(self.comment.blog.name, "Blog 1") 
#         self.assertEqual(self.comment.comment_body, "body") 
        
            
              