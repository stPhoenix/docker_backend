from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class BaseDateModel(model.Model):
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

class BaseTargetModel(BaseDateModel):
    target_related_name = "target_set"
    target = models.ForeignKey(UserModel, related_name=target_related_name) 

class UserModel(AbstractBaseUser):
    avatar = models.ImageField(upload_to="avatars/")
    banner = models.ImageField(upload_to="banners/")

    subscriptions = models.ManyToManyField('self', symmetrical=False)

class SubscriptionRequestModel(BaseTargetModel):
    target_related_name="subscription_requests"
    author = models.ForeignKey(UserModel, related_name="+") 

class SystemMessageModel(BaseTargetModel):
    text = models.CharField(max_length=120, null=False)
    read = models.BooleanField(default=False)
    target_related_name="system_messages"