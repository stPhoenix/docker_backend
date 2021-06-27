from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework import serializers

from social.models import UserModel, SubscriptionRequestModel
from social.serializers import CustomUserSerializer, SubscriptionRequestSerializer
from social.permissions import IsAuthorOrReadOnlyPermission, IsTargetPermission

# Create your views here.

class SubscriptionRequestBaseViewSet(ModelViewSet):
    serializer_class = SubscriptionRequestSerializer
    permission_classes = (IsAuthenticated, IsTargetPermission)

    def perform_update(self, serializer):
        if serializer.validated_data["status"] == SubscriptionRequestModel.Statuses.ACCEPTED:
            print("Accept")
            serializer.instance.accept()
        elif serializer.validated_data["status"] == SubscriptionRequestModel.Statuses.DENIED:
            serializer.instance.deny()
        return super().perform_update(serializer)

    def perform_create(self, serializer):
        target = serializer.validated_data["target"]

        if target == self.request.user:
            raise serializers.ValidationError("Can't send request to myself")

        already_sent = SubscriptionRequestModel.objects.filter(target=target).filter(author=self.request.user)
        if len(already_sent) != 0:
            raise serializers.ValidationError("Request already exists")
        
        serializer.validated_data["author"] = self.request.user
        return super().perform_create(serializer)

class MySubsRequestsViewSet(SubscriptionRequestBaseViewSet):
    
    def get_queryset(self):
        return self.request.user.my_requests.all()

class ToMeSubsRequestsViewSet(SubscriptionRequestBaseViewSet):
    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def get_queryset(self):
        return self.request.user.subscription_requests.all()