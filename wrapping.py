from types import ModuleType
import sys
import subprocess


def wrapping(func):
    def wrapper():
        subprocess.run(args="clear")
        print(f"{'➖'*20}\n")
        func()
        print(f"\n{'➖'*20}")

    return wrapper


# Backward-compatible alias for older imports.
wraping = wrapping


class _CallableModule(ModuleType):
    def __call__(self, func):
        return wrapping(func)


sys.modules[__name__].__class__ = _CallableModule