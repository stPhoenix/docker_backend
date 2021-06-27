from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from base.models import BaseDateModel

# Create your models here.


class UserAccountManager(BaseUserManager):
    def create_user(self, email, username, avatar, banner, password=None):
        user = self.model(email=email, username=username,
                          avatar=avatar, banner=banner)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, avatar, banner, password=None):
        user = self.create_user(email, username, avatar, banner, password)
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


class SubscriptionRequestModel(BaseDateModel):
    class Statuses(models.IntegerChoices):
        PENDING = 1, "PENDING"
        ACCEPTED = 2, "ACCEPTED"
        DENIED = 3, "DENIED"
    status = models.PositiveSmallIntegerField(
        choices=Statuses.choices,
        default=Statuses.PENDING,
    )
    target = models.ForeignKey(
        UserModel, related_name="subscription_requests", on_delete=models.CASCADE)
    author = models.ForeignKey(
        UserModel, related_name="my_requests", on_delete=models.CASCADE)

    class Meta:
        ordering = ("-created",)

    def accept(self):
        if self.target not in self.author.subscriptions.all():
            self.author.subscriptions.add(self.target)
        self.status = self.Statuses.ACCEPTED
        self.save(update_fields=("status",))

    def deny(self):
        self.status = self.Statuses.DENIED
        self.save(update_fields=("status",))
