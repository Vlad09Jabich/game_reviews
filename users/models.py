from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models

BASE_USER_ROLE = "base_user"
VERIFIED_USER_ROLE = "verified_user"


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, nickname, password=None, **extra_fields):
        """Create and save a user with the given email, username,
        nickname, and password."""
        # Convert email to lowercase on user creation
        email = self.normalize_email(email).lower()

        user = self.model(
            email=email, username=username, nickname=nickname, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, email, username, nickname, password=None, **extra_fields
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

        return self.create_user(email, username, nickname, password, **extra_fields)


class Permission(models.Model):
    """Part of the RBAC system. Provides main business logic permissions"""

    codename = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.codename


class Role(models.Model):
    """Part of the RBAC system. Provides main business logic roles"""

    name = models.CharField(unique=True, max_length=64)
    permission = models.ManyToManyField(Permission, related_name="roles")

    def __str__(self):
        return self.name


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

    def save(self, *args, **kwargs):
        """Save the current instance. Enforce business rules
        such as assingning the base user role."""

        if not self.pk and not self.role_id:
            self.role = Role.objects.get(name=BASE_USER_ROLE)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
