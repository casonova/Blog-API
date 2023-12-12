from rest_framework.test import APITestCase
from django.urls import reverse
from blog.models import Blog, Creator, Post, Comment
from accounts.models import User
from rest_framework.test import APIRequestFactory
from blog.views import *
from accounts.views import UserListAPIView
from rest_framework.test import APIClient


class TestView(APITestCase):
    
    
    factory = APIRequestFactory()
    
    # Urls of Views
    user_detail_url = reverse("user_detail")
    post_url = reverse('post')
    comment_url = reverse('comment')
    blog_url = reverse('blog-list')
    user_create_url = reverse("user_create")
    token = reverse("token_obtain_pair")
    
    # url = reverse("blog-detail")
    def setUp(self):
        
        self.user1 = User.objects.create(
                email="zainab@gmail.com",
                username="zainab",
                name="zainab",
                password="zainab"
            )
        
        self.user2 = User.objects.create(
                email="zubair@gmail.com",
                username="zubair",
                name="zubair",
                password="zubair",
                is_superuser=True, 
                is_staff=True
            )
        
        self.blog = Blog.objects.create(
                name="Blog 1"
            )
        
        self.creator = Creator.objects.create(user=self.user1)
        
        self.post = Post.objects.create(
                blog=self.blog,
                title="Sicology",
                body="Sicology",
                user_type=self.user1
            )
        self.comment = Comment.objects.create(
                post = self.post, 
                blog=self.blog, 
                user_type=self.user2, 
                comment_body="body"
            )
        
        
        self.user_data = {
            "email":"ali@gmail.com",
            "username":"ali",
            "name":"ali",
            "password":"ali"
            
        }
        
        self.blog_data ={
            "name":"Blog3",
            "posts":[
                {
                    "title":"Sicology",
                    "body":"Sicology",
                    "user_type":1
                }
            ],
            "comments":[
                    {
                        "post":1,
                        "comment_body":"Youtube",
                        "user_type":2
                    }
                ]
        }
        
        self.update_blog_data = {
            "name":"Blog3",
            "posts":[
                {
                    "title":"Sicology",
                    "body":"Sicology",
                    "user_type":1
                }
            ],
            "comments":[
                    {
                        "post":1,
                        "comment_body":"Spaceship",
                        "user_type":2
                    }
                ]
        }
        
        self.post_data = {
            "blog":1,
            "title":"Terminology",
            "body":"sicology",
            "user_type":1
        }
        
        self.comment_data = {
            "blog":1,
            "post":1,
            "comment_body":"sicology",
            "user_type":2
        }
        
        self.client = APIClient()
        data = {"email": self.user2.email, "password": "zubair" }
        response = self.client.post(self.token, data, format="json")
        self.token1 = response.data.get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token1}")
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown() 
    
    #=========== GET Request API Test ============================#
    def test_get_user(self):    
        request_user =self.factory.get(self.user_detail_url)
        user_view = UserListAPIView.as_view()
        responce = user_view(request_user)
        self.assertEqual(responce.status_code, 200)

        
    def test_get_post_with_authenticated(self):
        responce = self.client.get(self.post_url)
        self.assertEqual(responce.status_code, 200)    
    
    def test_get_post_with_unauthenticated(self):
        client = APIClient()
        responce = client.get(self.post_url)
        self.assertEqual(responce.status_code, 401)    
        
    def test_get_comment(self):
        responce = self.client.get(self.comment_url)
        self.assertEqual(responce.status_code, 200)  
        
    def test_get_blog(self):
        
        responce = self.client.get(self.blog_url)
        self.assertEqual(responce.status_code, 200)   
        
    #=========== POST Request API Test ============================#     
        
    def test_create_blog(self):
        responce = self.client.post(self.blog_url, self.blog_data, format="json")
        self.assertEqual(responce.status_code, 201) 
        
    def test_create_blog_unauthenticated(self):
        client = APIClient()
        responce = client.post(self.blog_url, self.blog_data, format="json")
        self.assertEqual(responce.status_code, 401) 
            
    def test_create_post(self):
        responce = self.client.post(self.post_url, self.post_data, format="json")
        self.assertEqual(responce.status_code, 201)    
        
    def test_create_post_unauthenticated(self):
        client = APIClient()
        responce = client.post(self.post_url, self.post_data, format="json")
        self.assertEqual(responce.status_code, 401)            
        
    def test_create_comment(self):
        request_comment = self.factory.post(self.comment_url, data=self.comment_data, format="json")
        comment_view = CommentApiView.as_view()
        responce = comment_view(request_comment)
        self.assertEqual(responce.status_code, 201)    
        
    #================= Update Request API Test ==================#    
        
    def test_update_blog_data_patch_authenticated(self):
        
        url = reverse("blog-detail", kwargs={'pk': self.blog.pk})
        responce = self.client.patch(url, self.update_blog_data, format="json")
        self.assertEqual(responce.status_code, 200)   
        
    def test_update_blog_data_patch_unauthenticated(self):
        client = APIClient()
        url = reverse("blog-detail", kwargs={'pk': self.blog.pk})
        responce = client.patch(url, self.update_blog_data, format="json")
        self.assertEqual(responce.status_code, 401)       
        
    def test_update_blog_data_put_authenticated(self):
        data = {
            "name":"Blog3",
            "posts":[
                {
                    "title":"Terminator",
                    "body":"Terminator",
                    "user_type":1
                }
            ],
            "comments":[
                    {
                        "post":1,
                        "comment_body":"Terminator",
                        "user_type":2
                    }
                ]
        }
        url = reverse("blog-detail", kwargs={'pk': self.blog.pk})
        responce = self.client.patch(url, data, format="json")
        self.assertEqual(responce.status_code, 200) 
            
    def test_update_blog_data_put_authenticated(self):
        client = APIClient()
        data = {
            "name":"Blog3",
            "posts":[
                {
                    "title":"Terminator",
                    "body":"Terminator",
                    "user_type":1
                }
            ],
            "comments":[
                    {
                        "post":1,
                        "comment_body":"Terminator",
                        "user_type":2
                    }
                ]
        }
        url = reverse("blog-detail", kwargs={'pk': self.blog.pk})
        responce = client.patch(url, data, format="json")
        self.assertEqual(responce.status_code, 401) 
        
    #================= Delete Request API Test ==================#      
     
    def test_delete_blog(self):
        url = reverse("blog-detail", kwargs={'pk': self.blog.pk})
        responce = self.client.delete(url)
        self.assertEqual(responce.status_code, 204) 
                