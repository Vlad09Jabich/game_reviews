from functools import wraps

from django.shortcuts import redirect


def anonymous_only(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):

        if request.user.is_authenticated:
            return redirect("main:hub")

        return func(request, *args, **kwargs)

    return wrapper
