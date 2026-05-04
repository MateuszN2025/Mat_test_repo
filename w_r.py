from types import ModuleType
import sys
import subprocess


def w_r(func):
    def wrapper():
        subprocess.run(args="clear")
        print(f"{'➖'*20}\n")
        func()
        print(f"\n{'➖'*20}")

    return wrapper


# Backward-compatible aliases for older imports.
wrapping = w_r
wraping = w_r


class _CallableModule(ModuleType):
    def __call__(self, func):
        return w_r(func)


sys.modules[__name__].__class__ = _CallableModule