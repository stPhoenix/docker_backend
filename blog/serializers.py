from rest_framework import serializers

from blog.models import PostModel, CommentModel, RateModel

class PostSerializer(serializers.ModelSerializer):
    comments__count = serializers.IntegerField(read_only=True)
    rating__rate__avg = serializers.IntegerField(read_only=True)
    rating__count = serializers.IntegerField(read_only=True)


    class Meta:
        model = PostModel
        fields = ("__all__")
        read_only_fields= ("author",)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = ("__all__")
        read_only_fields= ("author",)


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateModel
        fields = ("__all__")
        read_only_fields= ("author",)