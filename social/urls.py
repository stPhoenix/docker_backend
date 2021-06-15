from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter

from social.views import  SubscriptionRequestViewSet, SystemMessageViewset


router = DefaultRouter()
router.register(r"subscriptions", viewset=SubscriptionRequestViewSet, basename="subscriptions")
router.register(r"messages", viewset=SystemMessageViewset, basename="messages")

urlpatterns = [
    path("", include("djoser.urls")),
    path("", include('djoser.urls.authtoken')),
    path("", include("djoser.urls.jwt")),
    path("", include(router.urls)),
]