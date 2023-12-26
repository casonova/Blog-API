from django.urls import include, path
from rest_framework.routers import DefaultRouter

from blog.views import BlogVIewSet, CommentApiView, PostApiView

router = DefaultRouter()
router.register(r"posts", BlogVIewSet, basename="blog")
urlpatterns = [
    path("", include(router.urls), name="blog"),
    path("post", PostApiView.as_view(), name="post"),
    path("comment", CommentApiView.as_view(), name="comment"),
]
