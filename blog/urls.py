from django.urls import path, include
from rest_framework.routers import DefaultRouter

from blog.views import PostViewSet, CommentViewSet, RateViewSet

router = DefaultRouter()
router.register(r"posts", viewset=PostViewSet, basename="posts")
router.register(r"comments", viewset=CommentViewSet, basename="comments")
router.register(r"rates", viewset=RateViewSet, basename="rates")


urlpatterns = [
    path("", include(router.urls)),
]