from rest_framework import serializers

from blog.models import PostModel, CommentModel, RateModel


class ShortPostSerializer(serializers.ModelSerializer):
    comments__count = serializers.IntegerField(read_only=True)
    rating__rate__avg = serializers.IntegerField(read_only=True)
    rating__count = serializers.IntegerField(read_only=True)

    avatar = serializers.ImageField(source="author.avatar", read_only=True)
    banner = serializers.ImageField(source="author.banner", read_only=True)
    author_name = serializers.CharField(source="author.username", read_only=True)

    class Meta:
        model = PostModel
        exclude = ("text",)
        read_only_fields = ("author",)


class DetailPostSerializer(ShortPostSerializer):
    class Meta:
        model = PostModel
        fields = "__all__"
        read_only_fields = ("author",)


class CommentSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(source="author.avatar", read_only=True)
    author_name = serializers.CharField(source="author.username", read_only=True)

    class Meta:
        model = CommentModel
        fields = "__all__"
        read_only_fields = ("author",)


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateModel
        fields = "__all__"
        read_only_fields = ("author",)
