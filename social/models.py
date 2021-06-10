from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class User(AbstractBaseUser):
    avatar = models.ImageField(upload_to="avatars/")
    banner = models.ImageField(upload_to="banners/")

    subscriptions = models.ManyToManyField('self')

class SubscriptionRequestModel(models.Model):
    author = models.ForeignKey(User, related_name="+")
    target = models.ForeignKey(Userm related_name="subscription_requests")
    date = models.DateField(auto_now_add=True) 

class SystemMessageModel(models.Model):
    date = models.DateField(auto_now_add=True)
    text = models.CharField(max_length=120, null=False)
    read = models.BooleanField(default=False)
    target = models.ForeignKey(User, related_name="system_messages")