from django.urls import include, path
from rest_framework.routers import DefaultRouter

from blog.views import BlogVIewSet, PostApiView, CommentViewSet

router = DefaultRouter()
router.register(r"blog", BlogVIewSet, basename="blog")
router.register(r"comment", CommentViewSet, basename="comment")
urlpatterns = [
    path("", include(router.urls),),
    path("post", PostApiView.as_view(), name="post"),
    path("post/<int:pk>/", PostApiView.as_view(), name="post"),
    # path("comment", CommentApiView.as_view(), name="comment"),
    # path("comment/<int:pk>", CommentApiView.as_view(), name="comment"),
]
