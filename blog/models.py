from django.db import models

from base.models import BaseDateModel, BaseTextDateModel
from social.models import UserModel

# Create your models here.


class PostModel(BaseTextDateModel):
    author = models.ForeignKey(
        UserModel, related_name="posts", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=120, default="Post Title")


class CommentModel(BaseTextDateModel):
    author = models.ForeignKey(
        UserModel, related_name="comments", on_delete=models.SET_NULL, null = True
    )
    post = models.ForeignKey(
        PostModel, related_name="comments", on_delete=models.CASCADE
    )


class RateModel(BaseDateModel):
    class Marks(models.IntegerChoices):
        MINIMAL = 1, "MINIMAL"
        ACCEPTED = 2, "ACCEPTED"
        NORMAL = 3, "NORMAL"
        GOOD = 4, "GOOD"
        GREAT = 5, "GREAT"

    rate = models.PositiveSmallIntegerField(choices = Marks.choices, default=Marks.MINIMAL)
    post = models.ForeignKey(PostModel, related_name="rating", on_delete=models.CASCADE)
    author = models.ForeignKey(UserModel, related_name="+", on_delete=models.SET_NULL, null=True)
