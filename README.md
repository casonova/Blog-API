
# Blog Project


This Django REST framework project provides API endpoints for managing posts, blogs, and comments with specific functionalities and permissions. It includes ViewSets and APIViews for CRUD operations on Post, Blog, and Comment models.

# Project Components
1. Views
- PostApiView
    
    Description: Handles CRUD operations for the Post model.

    Endpoints:
    - GET: Retrieve a list of all posts.
    - POST: Create a new post.
    - PUT: Update a specific post by ID.
   - PATCH: Partially update a specific post by ID.
    - DELETE: Delete a specific post by ID.
- Permissions:
    
    Only logged-in users (IsLoggedIn) are allowed to access these endpoints.
- BlogViewSet
    
    Description: Provides a ViewSet for the Blog model, enabling CRUD operations.
    
    Endpoints:
    - GET: Retrieve a list of all blogs.
    - POST: Create a new blog.
    - PUT, PATCH, DELETE: Update and delete operations for blogs.
- Permissions:
    
    Admin users (IsAdminUser) have access to these endpoints.
- CommentViewSet
    
    Description: Manages the Comment model through a ViewSet.
    - Endpoints:
    - GET: Fetch a list of all comments.
    - POST: Create a new comment.
    - PUT, PATCH, DELETE: Update and delete operations for comments.
- Permissions:
    
    Only logged-in users (IsLoggedIn) have access to these endpoints.
- Serializers
    - PostSerializer: Serializes and deserializes Post model data.
    - BlogSerializer: Serializes and deserializes Blog model data.
    - CommentSerializer: Handles serialization and deserialization of Comment model data.
- Permissions
    - IsAdminUser: Permission class allowing only admin users access to specific views.
    - IsLoggedIn: Permission class restricting access to logged-in users for certain views.








## Installation
To install and run the project locally, follow the steps:

1. Clone the repository:


```bash
https://github.com/casonova/Blog-API.git
```
2. Make Virtual environment:

```bash
python3 -m venv env
```  

3. Install dependencies:

```bash
pip install -r requirements.txt
```    
4. Apply database migrations:
```bash
python manage.py makemigrations
```  

```bash
python manage.py migrate
```    
5. Run server
 ```
 python manage.py runserver
 ```

 
 
## Usage
1. Create a superuser:

```javascript
python manage.py createsuperuser
```


## Credits

- [Django Framework](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)





