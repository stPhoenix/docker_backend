from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer

from social.models import UserModel, SubscriptionRequestModel


class CustomUserSerializer(UserSerializer):
    class Meta:
        model = UserModel
        exclude = ("password", "last_login")
        read_only_fields = ("subscriptions",)

class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = UserModel
        exclude = ("subscriptions", "last_login", "is_staff")

class SubscriptionRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionRequestModel
        fields = ("__all__")
        read_only_fields= ("author",)