from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class UserAccountManager(BaseUserManager):
    def create_user(self, email, username, avatar, banner, password=None):
        user = self.model(email=email, username=username, avatar=avatar, banner=banner)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email, username, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username_):
        return self.get(username=username_)

class UserModel(AbstractBaseUser):
    avatar = models.ImageField(upload_to="avatars/")
    banner = models.ImageField(upload_to="banners/")
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    subscriptions = models.ManyToManyField('self', symmetrical=False)

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ("email", "avatar", "banner", "password")

class BaseDateModel(models.Model):
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)


class BaseTargetModel(BaseDateModel):
    target_related_name = "target_set"
    target = models.ForeignKey(UserModel, related_name=target_related_name, on_delete=models.CASCADE)


class SubscriptionRequestModel(BaseTargetModel):
    target_related_name = "subscription_requests"
    author = models.ForeignKey(UserModel, related_name="+", on_delete=models.CASCADE)


class SystemMessageModel(BaseTargetModel):
    text = models.CharField(max_length=120, null=False)
    read = models.BooleanField(default=False)
    target_related_name = "system_messages"
