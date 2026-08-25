from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models

from main.models import Game


class CustomUserManager(BaseUserManager):
    def create_user(self, username, nickname, email, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(
            username=username, nickname=nickname, email=email, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, username, nickname, email, password=None, **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")
        return self.create_user(username, nickname, email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=64)
    nickname = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    fan = models.ManyToManyField(Game)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["nickname", "email"]

    def __str__(self):
        return self.username
