from rest_framework import serializers

from social.models import UserModel, SubscriptionRequestModel, SystemMessageModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ("__all__")

class UserCreateSerializer(serializers.ModelSerializer):
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