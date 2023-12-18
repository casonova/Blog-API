from rest_framework.test import APITestCase
from django.urls import reverse
from blog.models import Blog, Post, Comment
from accounts.models import User
from rest_framework.test import APIRequestFactory
from blog.views import *
from accounts.views import UserListAPIView
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

class TestView(APITestCase):
    
    
    factory = APIRequestFactory()
    
    # Urls of Views
    user_detail_url = reverse("user_detail")
    post_url = reverse('post')
    blog_url = reverse('blog-list')
    user_create_url = reverse("user_create")
    token = reverse("token_obtain_pair")
    login_url = reverse("login")
    logout_url = reverse("logout")
    
    # url = reverse("blog-detail")
    def setUp(self):
        
        self.user1 = User.objects.create(
                email="zainab@gmail.com",
                username="zainab",
                name="zainab",
                password="zainab",
                action_choice="creator"
                
            )
        
        self.user2 = User.objects.create(
                email="zubair@gmail.com",
                username="zubair",
                name="zubair",
                password="zubair",
                action_choice="visitor",
                is_superuser=True, 
                is_staff=True
            )
        
        self.blog = Blog.objects.create(
                name="Blog 1"
            )
        
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
        self.refresh_token = response.data.get("refresh")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token1}")
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown() 
    
    # =========== GET Request API Test ============================#
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
        url = reverse("comment-list")
        responce = self.client.get(url)
        self.assertEqual(responce.status_code, 200)  
        
    def test_get_blog(self):
        
        responce = self.client.get(self.blog_url)
        self.assertEqual(responce.status_code, 200)   
        
    # =========== POST Request API Test ============================#   
    
    def test_create_user(self):
        client = APIClient()
        data = {
            "email": "admin@gmail.com",
            "username":"admin",
            "name":"admin",
            "password":"admin",
            "action_choice":"admin"
        }  
        responce = client.post(self.user_create_url, data, format="json")
        self.assertEqual(responce.status_code, 201)
    def test_create_blog(self):
        responce = self.client.post(self.blog_url, self.blog_data, format="json")
        self.assertEqual(responce.status_code, 201) 
        
    def test_create_blog_unauthenticated(self):
        client = APIClient()
        responce = client.post(self.blog_url, self.blog_data, format="json")
        self.assertEqual(responce.status_code, 401) 
            
    def test_create_post(self):
        responce = self.client.post(self.post_url, self.post_data, format="json")
        # import pdb; pdb.set_trace()
        self.assertEqual(responce.status_code, 201)    
        
    def test_create_post_unauthenticated(self):
        client = APIClient()
        responce = client.post(self.post_url, self.post_data, format="json")
        self.assertEqual(responce.status_code, 401)            
        
    def test_create_comment(self):
        url = reverse("comment-list")
        request_comment = self.factory.post(url, data=self.comment_data, format="json")
        comment_view = CommentViewSet.as_view({'post': 'list'})
        responce = comment_view(request_comment)
        # import pdb; pdb.set_trace()
        self.assertEqual(responce.status_code, 200)    
        
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
        
    def test_update_post_data_put_authenticated(self):
        data = {
            "blog":1,
            "title":"Narnia",
            "body":"Sicology",
            "user_type":1
        }
        url = reverse("post", kwargs={'pk': self.post.pk})
        responce = self.client.put(url, data, format="json")
        self.assertEqual(responce.status_code, 200)  
        
    def test_update_post_data_patch_authenticated(self):
        data = {
            "blog":1,
            "title":"Narnia",
            "body":"Sicology",
            "user_type":1
        }
        url = reverse("post", kwargs={'pk': self.post.pk})
        responce = self.client.patch(url, data, format="json")
        self.assertEqual(responce.status_code, 200)     
            
    def test_update_post_data_put_unauthenticated(self):
        client = APIClient()
        data = {
            "blog":1,
            "title":"Narnia",
            "body":"Sicology",
            "user_type":1
        }
        url = reverse("post", kwargs={'pk': self.post.pk})
        responce = client.put(url, data, format="json")
        self.assertEqual(responce.status_code, 401)    
        
    def test_update_post_data_patch_unauthenticated(self):
        client = APIClient()
        data = {
            "blog":1,
            "title":"Narnia Lullabay",
            "body":"Sicology",
            "user_type":1
        }
        url = reverse("post", kwargs={'pk': self.post.pk})
        responce = client.put(url, data, format="json")
        self.assertEqual(responce.status_code, 401)   
       
    def test_update_comment_data_put_authenticated(self):  
        data = {
            "post":1,
            "comment_body":"Youtube",
            "user_type":2
        }
        url = reverse("comment-detail", kwargs={'pk': self.comment.pk})  
        responce = self.client.put(url, data, format="json") 
        # import pdb; pdb.set_trace()
        self.assertEqual(responce.status_code, 200) 
        
    def test_update_comment_data_patch_authenticated(self):  
        data = {
            "post":1,
            "comment_body":"Billa",
            "user_type":2
        }
        url = reverse("comment-detail", kwargs={'pk': self.comment.pk})  
        responce = self.client.put(url, data, format="json") 
        # import pdb; pdb.set_trace()
        self.assertEqual(responce.status_code, 200)     
        
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
                
    def test_delete_post(self):
        url = reverse("post", kwargs={'pk': self.post.pk})
        responce = self.client.delete(url)
        self.assertEqual(responce.status_code, 200) 
    
    def test_delete_comment(self):
        url = reverse("comment-detail", kwargs={'pk': self.comment.pk})
        responce = self.client.delete(url)
        self.assertEqual(responce.status_code, 204)  

      #============== Account views testcases ================#
    def test_valid_login(self):
        client = APIClient()
          
        data = {
            "email": "zainab@gmail.com",
            "password": "zainab"
            }
        response = client.post(self.login_url, data, format="json")  
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_200_OK)  
        self.assertIn('refresh', response.data)
        self.assertIn('access', response.data)  
        
    def test_invalid_login_wrong_credentials(self):
        client = APIClient()
        data = {
            'email': 'test@gmail.com',
            'password': 'test'
        }
        response = client.post(self.login_url, data, format="json") 
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_invalid_logout_missing_token(self):
        client = APIClient()
        response = client.post(self.logout_url, {})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)  
        
    def test_invalid_logout_token(self):
        data ={
            "refresh":self.refresh_token
        }
        response = self.client.post(self.logout_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_205_RESET_CONTENT)      

               
