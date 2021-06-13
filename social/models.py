from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class BaseDateModel(model.Model):
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

class User(AbstractBaseUser):
    avatar = models.ImageField(upload_to="avatars/")
    banner = models.ImageField(upload_to="banners/")

    subscriptions = models.ManyToManyField('self', symmetrical=False)

class SubscriptionRequestModel(BaseDateModel):
    author = models.ForeignKey(User, related_name="+")
    target = models.ForeignKey(User, related_name="subscription_requests") 

class SystemMessageModel(BaseDateModel):
    text = models.CharField(max_length=120, null=False)
    read = models.BooleanField(default=False)
    target = models.ForeignKey(User, related_name="system_messages")