from rest_framework import serializers

from blog.models import PostModel, CommentModel, RateModel

class PostSerializer(serializers.ModelSerializer):
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


class AddRateSerializer(RateSerializer):
    def is_valid(self, raise_exception=False):
        condition =  super().is_valid(raise_exception=raise_exception)
        if condition == False: return condition

        try:
            RateModel.objects.get(author = self.validated_data["author"])
            raise serializers.ValidationError("You've already rated this post")
        except Exception:
            pass
        
        return condition