from functools import wraps
import subprocess
subprocess.run(args="clear")
print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n")


def deco(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        WRAPPER !
        """
        print("W1")
        func(*args, **kwargs)
        print("W2") 
    return wrapper

def deco2(func):
    def wrapper2(*args, **kwargs):
        """
        WRAPPER 2 !
        """
        print("W1")
        func(*args, **kwargs)
        print("W2") 
    return wrapper2
        

@deco
def hello():
    """
    This is hello func
    """
    print("hello")
    pass

@deco2
def yellow():
    """
    This is yellow func
    """
    print("yellow")
    pass

hello()
print(hello.__doc__)
print(hello.__name__)
print("------------------------------------------")
yellow()
print(yellow.__doc__)
print(yellow.__name__)


# without wraps from functools: WRAPPER !
# @wraps preserves these attributes from the wrapped function:
        # __name__ — function name
        # __qualname__ — qualified name
        # __doc__ — docstring
        # __dict__ — attribute dictionary
        # __module__ — module name
        # __annotations__ — type annotations
        # __wrapped__ — reference to the original function (added by wraps itself)


print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")  # noqa: E303

    