from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers

from social.models import SubscriptionRequestModel, UserModel


class CustomUserSerializer(UserSerializer):
    class Meta:
        model = UserModel
        exclude = ("password", "last_login")
        read_only_fields = ("subscriptions",)


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = UserModel
        exclude = ("subscriptions", "last_login", "is_staff")


class CustomUserListSerializer(CustomUserSerializer):
    class Meta:
        model = UserModel
        exclude = (
            "subscriptions",
            "banner",
            "email",
            "is_staff",
            "password",
            "last_login",
        )


class SubscriptionRequestSerializer(serializers.ModelSerializer):
    status_text = serializers.CharField(source="get_status_display", read_only=True)

    class Meta:
        model = SubscriptionRequestModel
        fields = "__all__"
        read_only_fields = ("author",)


class MySubscriptionRequestSerializer(SubscriptionRequestSerializer):
    target_username = serializers.CharField(source="target.username", read_only=True)

    class Meta:
        model = SubscriptionRequestModel
        fields = "__all__"
        read_only_fields = ("author", "status")


class ToMeSubscriptionRequestSerializer(SubscriptionRequestSerializer):
    author_username = serializers.CharField(source="author.username", read_only=True)

    class Meta:
        model = SubscriptionRequestModel
        fields = "__all__"
        read_only_fields = ("author",)
