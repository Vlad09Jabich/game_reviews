from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(
        self, email, role, username, nickname, password=None, **extra_fields
    ):
        # Convert email to lowercase on registration
        email = self.normalize_email(email).lower()

        user = self.model(
            email=email, role=role, username=username, nickname=nickname, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, email, username, nickname, role=None, password=None, **extra_fields
    ):
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_active") is not True:
            raise ValueError("Superuser must have is_active=True")
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self.create_user(
            email, role, username, nickname, password, **extra_fields
        )


class Permission(models.Model):
    codename = models.CharField(unique=True, max_length=100)


class Role(models.Model):
    name = models.CharField(unique=True, max_length=64)
    permission = models.ManyToManyField(Permission, related_name="roles")


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Email as login for identification, password for authentication,
    role for authorization in Role-Based Access Control system.
    Nickname is used as a non-unique public display name,
    while username is a unique user identifier visible to other users.
    """

    email = models.EmailField(unique=True, max_length=254)

    role = models.ForeignKey(
        Role, on_delete=models.SET_NULL, null=True, blank=True, related_name="users"
    )

    username = models.CharField(unique=True, max_length=64)
    nickname = models.CharField(max_length=64)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "nickname"]

    def __str__(self):
        return self.username
