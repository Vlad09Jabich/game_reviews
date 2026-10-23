from .models import VERIFIED_USER_ROLE, CustomUser, Role

__all__ = [
    "get_user_role",
    "check_user_permission",
    "verify_user_account",
]


def get_user_role(user_id: int) -> str | None:
    """Get the string name of the user's role."""
    try:
        # Efficiently get user and role objects using JOIN
        user = CustomUser.objects.select_related("role").get(id=user_id)
        return user.role.name
    except CustomUser.DoesNotExist:
        return None


def verify_user_account(user_id: int) -> bool:
    """Upgrade user's role to 'verified_user'"""
    try:
        user = CustomUser.objects.get(id=user_id)
        verified_role = Role.objects.get(name=VERIFIED_USER_ROLE)

        user.role = verified_role
        user.save(update_fields=["role"])
        return True
    except user.DoesNotExist:
        return False


def check_user_permission(user_id: int, perm_codename: str) -> bool:
    """Check if the user has a specific permission."""
    try:
        # Fetch user, role, and their permissions into memory using JOIN/prefetch
        user = (
            CustomUser.objects.select_related("role")
            .prefetch_related("role__permission")
            .get(id=user_id)
        )

        # Iterate over the prefetched permissions QuerySet to find the match
        for perm in user.role.permission.all():
            if perm.codename == perm_codename:
                return True

        return False

    except CustomUser.DoesNotExist:
        return False
