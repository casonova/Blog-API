from django.urls import include, path
from rest_framework.routers import DefaultRouter

from blog.views import BlogVIewSet, CommentApiView, PostApiView

router = DefaultRouter()
router.register(r"posts", BlogVIewSet, basename="post")
urlpatterns = [
    path("", include(router.urls)),
    path("create", PostApiView.as_view(), name="post"),
    path("comment", CommentApiView.as_view(), name="comment"),
    path("auth/", include("rest_framework.urls", namespace="rest_framework")),
]
