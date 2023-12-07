from django.urls import path, include
from blog.views import PostApiView, CommentApiView, BlogVIewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'posts', BlogVIewSet, basename="post")
urlpatterns = [
    path("", include(router.urls)),
    path("create", PostApiView.as_view(), name="post"),
    path("comment", CommentApiView.as_view(), name="comment"),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]