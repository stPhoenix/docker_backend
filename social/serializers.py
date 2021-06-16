from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer

from social.models import UserModel, SubscriptionRequestModel, SystemMessageModel


class CustomUserSerializer(UserSerializer):
    class Meta:
        model = UserModel
        exclude = ("password", "last_login")

class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = UserModel
        exclude = ("subscriptions", "last_login")

class SubscriptionRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionRequestModel
        fields = ("__all__")

class SystemMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemMessageModel
        fields = ("__all__")