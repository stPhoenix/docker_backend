from django.db.models import Avg, Count
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework.viewsets import ModelViewSet

from blog.models import CommentModel, PostModel, RateModel
from blog.permissions import (
    IsAuthorOnlyPermission,
    IsAuthorOrReadOnlyPermission,
    isSubscriberPermission,
)
from blog.serializers import (
    CommentSerializer,
    DetailPostSerializer,
    RateSerializer,
    ShortPostSerializer,
)


class BasePostViewSet(ModelViewSet):
    serializer_class = DetailPostSerializer
    permission_classes = (IsAuthenticated, IsAuthorOrReadOnlyPermission)

    def get_queryset(self):
        author = self.request.user.subscriptions.all()
        if self.action == "my":
            author = (self.request.user,)
        elif self.action == "user":
            author = (self.request.pk,)
        return PostModel.objects.filter(author__in=author).annotate(
            Count("comments"), Avg("rating__rate"), Count("rating")
        )

    def list(self, request, *args, **kwargs):
        self.serializer_class = ShortPostSerializer
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.validated_data["author"] = self.request.user
        return super().perform_create(serializer)


class PostViewSet(BasePostViewSet):
    def get_queryset(self):
        author = self.request.user.subscriptions.all()
        if self.action == "user":
            author = (self.request.pk,)
        return PostModel.objects.filter(author__in=author).annotate(
            Count("comments"), Avg("rating__rate"), Count("rating")
        )

    @action(detail=False, url_path="user/(?P<pk>[^/.]+)")
    def user(self, request, pk=None):
        if len(self.request.user.subscriptions.filter(pk=pk)) == 0:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        self.request.pk = pk
        return self.list(request)


class MyPostViewSet(BasePostViewSet):
    def get_queryset(self):
        return PostModel.objects.filter(author=self.request.user).annotate(
            Count("comments"), Avg("rating__rate"), Count("rating")
        )


class BasePostAdditionViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, IsAuthorOnlyPermission)

    def perform_create(self, serializer):
        serializer.validated_data["author"] = self.request.user
        if not isSubscriberPermission(
            serializer.validated_data["post"].author, request=self.request
        ):
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().perform_create(serializer)


class CommentViewSet(BasePostAdditionViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        if self.action == "post_comments":
            return CommentModel.objects.filter(
                post__author__in=self.request.user.subscriptions.all()
            ).filter(post=self.request.pk)
        return CommentModel.objects.filter(author=self.request.user)

    @action(detail=False, url_path="post/(?P<pk>[^/.]+)")
    def post_comments(self, request, pk=None):
        self.request.pk = pk
        return self.list(request)


class RateViewSet(BasePostAdditionViewSet):
    serializer_class = RateSerializer

    def get_queryset(self):
        return RateModel.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        rates = RateModel.objects.filter(author=self.request.user)
        if len(rates) != 0:
            raise ValidationError("You've already rated this post")
        return super().perform_create(serializer)
