from django.urls import include, path
from rest_framework.routers import DefaultRouter

from social.views import (
    MySubsRequestsViewSet,
    SearchUserViewSet,
    ToMeSubsRequestsViewSet,
)

router = DefaultRouter()
router.register(
    r"subscriptions/my", viewset=MySubsRequestsViewSet, basename="my_subscriptions"
)
router.register(
    r"subscriptions/to-me", viewset=ToMeSubsRequestsViewSet, basename="my_subscriptions"
)
router.register(r"search", viewset=SearchUserViewSet, basename="search_user")

urlpatterns = [
    path("", include("djoser.urls")),
    path("", include("djoser.urls.jwt")),
    path("", include(router.urls)),
]
