"""Decorators used by the demo application."""

from functools import wraps
import subprocess


def wrapping(func):
    """Decorate a function by clearing the terminal and framing its output.

    ``functools.wraps`` preserves metadata such as the wrapped function's name
    and docstring. That becomes important in larger projects for debugging,
    introspection, and testing tools.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Passing arguments as a list avoids shell parsing and keeps the system
        # call explicit.
        subprocess.run(["clear"], check=False)

        # The visual separators make it easy to spot the wrapped section of the
        # program output when running the example interactively.
        print("➖" * 20)
        result = func(*args, **kwargs)
        print("➖" * 20)

        # Returning the wrapped function's result keeps the decorator reusable
        # for functions that compute values, not only for functions that print.
        return result

    return wrapper


# Keep the original misspelled name available so older exercise imports still
# work while newer code can use the corrected spelling.
wraping = wrapping