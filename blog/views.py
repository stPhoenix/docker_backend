from django.db.models import Avg, Count

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from blog.serializers import PostSerializer, CommentSerializer, RateSerializer, AddRateSerializer
from blog.models import PostModel, CommentModel, RateModel
from blog.permissions import IsAuthorOrReadOnlyPermission, IsAuthorOnlyPermission

class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, IsAuthorOrReadOnlyPermission)

    def get_queryset(self):
        author = self.request.user.subscriptions.all()
        if self.action == "my":
            author = (self.request.user,)
        return PostModel.objects.filter(author__in=author).annotate(Count("comments"), Avg("rating__rate"), Count("rating"))
    
    @action(detail=False)
    def my(self, request):
        return self.list(request)

    def perform_create(self, serializer):
        serializer.validated_data["author"] = self.request.user
        return super().perform_create(serializer)

class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, IsAuthorOnlyPermission)

    def get_queryset(self):
        return CommentModel.objects.filter(author = self.request.user)


class RateViewSet(ModelViewSet):
    serializer_class = RateSerializer
    permission_classes = (IsAuthenticated, IsAuthorOnlyPermission)

    def get_queryset(self):
        return RateModel.objects.filter(author = self.request.user)
    
    def create(self, request, *args, **kwargs):
        self.serializer_class = AddRateSerializer
        return super().create(request, *args, **kwargs)
