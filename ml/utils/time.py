import time
from functools import wraps
from commont.logger import get_logger

logger = get_logger("training")

def measure_time(func):
    """Decorator to measure execution time of a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter_ns()
        result = func(*args, **kwargs)
        end = time.perf_counter_ns()
        elapsed_ns = end - start
        elapsed_s = elapsed_ns / 1e9

        if elapsed_s < 1:
            elapsed_ms = elapsed_s * 1000
            elapsed_str = f"{elapsed_ms:.2f} ms"
        elif elapsed_s < 60:
            elapsed_str = f"{elapsed_s:.2f} s"
        else:
            elapsed_min = elapsed_s / 60
            elapsed_str = f"{elapsed_min:.2f} min"

        logger.info(f"Function '{func.__name__}' executed in {elapsed_str}")
        return result
    return wrapper
