from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from backend.social.models import UserModel, SubscriptionRequestModel, SystemMessageModel
from backend.social.serializers import UserSerializer, SubscriptionRequestSerializer, SystemMessageSerializer
from backend.social.permissions import IsAuthorOrReadOnlyPermission

# Create your views here.
class UserViewSet(ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsAuthorOrReadOnlyPermission)