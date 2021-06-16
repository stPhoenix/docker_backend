from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response

from social.models import UserModel, SubscriptionRequestModel, SystemMessageModel
from social.serializers import CustomUserSerializer, SubscriptionRequestSerializer, SystemMessageSerializer
from social.permissions import IsAuthorOrReadOnlyPermission, IsTargetPermission

# Create your views here.

class SubscriptionRequestViewSet(ModelViewSet):
    serializer_class = SubscriptionRequestSerializer
    permission_classes = (IsAuthenticated, IsTargetPermission)

    def get_queryset(self):
        return self.user.subscription_requests.all()

    def destroy(self, request, *args, **kwargs):
        self.answer_sub_request(request)

        return super(SubscriptionRequestViewSet, self).destroy(request, *args, **kwargs)

    def answer_sub_request(self, request):
        obj = self.get_object()
        message = "User rejected your subscription request"
        if request.data["answer"] == "True":
            obj.author.subscriptions.add(request.user)
            message = "User accepted your subscription request"
        SystemMessageModel.objects.create(target=obj.target, text=message)


class SystemMessageViewset(ModelViewSet):
    serialzer_class = SystemMessageSerializer
    permission_classes = (IsAuthenticated, IsTargetPermission)

    def get_queryset(self):
        return self.request.user.system_messages.all()

    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
