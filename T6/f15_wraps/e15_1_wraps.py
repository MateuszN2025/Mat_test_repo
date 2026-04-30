from functools import wraps
import subprocess
subprocess.run(args="clear")
print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n")

def adder_with_wraps(func):
    @wraps(func)
    def wrapper1(*args, **kwargs):
        """
        wrapper1 __doc__
        """
        
        print("WRAPPER1⚠️")
        func()
    return wrapper1

def adder_no_wraps(func):
    def wrapper2(*args, **kwargs):
        """
        wrapper2 __doc__
        """
        
        print("WRAPPER2❌")
        func()
    return wrapper2

@adder_with_wraps
def blue_func():
    """
    🟦 blue_func __doc__
    """
    
    print(blue_func.__name__)
    print(blue_func.__doc__)
    
@adder_no_wraps    
def green_func():
    """
    🟩 green_func __doc__
    """
    
    print(green_func.__name__)
    print(green_func.__doc__)
    

blue_func()
print("------------------------------------------")
green_func()

print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")  # noqa: E303

