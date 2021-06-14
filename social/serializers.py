from rest_framework import serializers

from backend.social.models import UserModel, SubscriptionRequestModel, SystemMessageModel


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserModel
        fields = ("username", "email", "avatar", "banner")

class SubscriptionRequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubscriptionRequestModel
        fields = ("__all__")

class SystemMessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SystemMessageModel
        fields = ("__all__")