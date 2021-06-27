from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter

from social.views import  MySubsRequestsViewSet, ToMeSubsRequestsViewSet


router = DefaultRouter()
router.register(r"subscriptions/my", viewset=MySubsRequestsViewSet, basename="my_subscriptions")
router.register(r"subscriptions/to-me", viewset=ToMeSubsRequestsViewSet, basename="my_subscriptions")


urlpatterns = [
    path("", include("djoser.urls")),
    path("", include('djoser.urls.authtoken')),
    path("", include("djoser.urls.jwt")),
    path("", include(router.urls)),
]