from django.urls import include, path
from rest_framework.routers import DefaultRouter

from blog.views import CommentViewSet, MyPostViewSet, PostViewSet, RateViewSet

router = DefaultRouter()
router.register(r"posts/my", viewset=MyPostViewSet, basename="my-posts")
router.register(r"posts", viewset=PostViewSet, basename="posts")
router.register(r"comments", viewset=CommentViewSet, basename="comments")
router.register(r"rates", viewset=RateViewSet, basename="rates")


urlpatterns = [
    path("", include(router.urls)),
]
