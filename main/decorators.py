import time
from functools import wraps


def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        end_time = time.perf_counter()
        duration = end_time - start_time
        print(f"[TIME] Function {func.__name__} - duration {duration}", flush=True)
        return func(*args, **kwargs)
    return wrapper