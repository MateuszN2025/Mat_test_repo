import time


def func_wrapper1(func):

    def wrapper1(aa, bb):
        print("--------------")
        print(f"sumik: {func(aa, bb)}")
        print("--------------")

    return wrapper1

# func_wrapper is a higher-order function:
# (a function that accepts another function).
"""
    hat wrapper remembers the variable func.
    This is called a closure.
    So wrapper1 stores:
    "I remember func = original sumik"
"""


def func_wrapper2(func):
    def wrapper2(aa, bb):
        print("--------------")
        result = func(aa, bb)
        print(f">>>>>>>>: {result}")
        print("--------------")
        return result

    return wrapper2


@func_wrapper1
def sumik(a, b):
    return a + b

def mnoznik(a, b):
    return a * b


sumik(19,39) # wrapper1(19,39)
mnoznik(100,2)
# mnoznik = wrapper2 # NameError: name 'wrapper2' is not defined
mnoznik = func_wrapper2(mnoznik)
mnoznik(100,2)



# The name sumik NO LONGER points to original sumik.
# # It now points to wrapper1.

"""
After decoration:
sumik is NO LONGER the original function.
Now sumik becomes:
wrapper1
Now this happens:

sumik = wrapper1
"""


"""
These Two Are Identical
Version 1 (manual)
def mnoznik(a,b):
    return a*b

mnoznik = func_wrapper2(mnoznik)
Version 2 (decorator syntax)
@func_wrapper2
def mnoznik(a,b):
    return a*b

Python automatically transforms it into version 1 behind the scenes.
"""

"""
@app.route("/home")
def homepage():
    return "Hello"
---------------------------------
def homepage():
    return "Hello"
homepage = app.route("/home")(homepage)
---------------------------------
---------------------------------
@timer
@logger
@authenticate
def secret_function():
---------------------------------
secret_function = timer(
                    logger(
                        authenticate(secret_function)))
                        
                        
syntactic sugar - a prettier way to write existing logic.
"""

print("---------------------------------")
print("---------------------------------")
print("---------------------------------")

def logi(f):
    def w_logi():
        print(f"logi deco : f() : {f}")
        """
        It:
            prints f
            ends
        after print:
            w_logi finished
        """
    return w_logi

def nothing(f):
    def w_nothing():
        print(f"nothing deco: f() : {f}")
    return w_nothing

def anything(f):
    def w_anything():
        print(f"anything deco: f() : {f}")
    return w_anything

@logi
@nothing
@anything
def func1():
    pass

func1()

# secret_function = logi(
#                     nothing(
#                         anything(func1)))

# w_logi remembers f = w_nothing
# w_nothing remembers f = w_anything
# w_anything remembers f = original func1

# The real reason is:
# # w_logi never calls the next function (f), so execution stops there.


# Final value of func1 is:
# w_logi
# func1() means: w_logi()

"""
NOW YOU CALL:
secret_function()
which means:
w_logi()
"""

# print(time)
# print(time.time())
# print(time.time_ns())
# print(time.daylight)
# print(time.tm_hour)
# print(help(time))

# now = time.localtime()
# human_time = time.strftime("%Y-%m-%d %H:%M:%S", now)
#
# print(human_time)

print("---------------------------------")
print("---------------------------------")
print("---------------------------------")


import functools

def logging(funccc):
    # @functools.wraps(funccc) # It copies the metadata from funccc to logging_w
    def logging_w(*args, **kwargs):
        logging_w.__annotations__ = {"a":1}
        print("=============")
        print("     =============")
        print(f"    funccc.__name__ | {funccc.__name__}")
        print(f"    funccc.__doc__ | {funccc.__doc__}")
        print(f"    funccc.__module__ | {funccc.__module__}")
        print(f"    funccc.__annotations__ | {funccc.__annotations__}")
        print("     +++++++++++++")
        print(f"    logging_w.__name__ | {logging_w.__name__}")
        print(f"    logging_w.__doc__ | {logging_w.__doc__}")
        print(f"    logging_w.__module__ | {logging_w.__module__}")
        print(f"    logging_w.__annotations__ | {logging_w.__annotations__}")
        print("     =============")

        # =============
        #      =============
        #     funccc.__name__ | fun1
        #     funccc.__doc__ | None
        #     funccc.__module__ | __main__
        #     funccc.__annotations__ | {} <=========== with @functools.wraps
        #      +++++++++++++
        #     logging_w.__name__ | fun1
        #     logging_w.__doc__ | None
        #     logging_w.__module__ | __main__
        #     logging_w.__annotations__ | {'a': 1}
        #      =============

        print(f"args:{args} kwargs:{kwargs}")
        print("=============")
        t1 = time.time_ns()
        result = funccc(*args, **kwargs)
        t2 = time.time_ns()
        td = ((t2-t1)/1_000_000_000)
        print(f"Function duration: {td:.3f} sec")
        return result
    return logging_w

"""
When you decorate a wrapper like this:
def logging_w(*args, **kwargs):
    return funccc(*args, **kwargs)
    
Python forgets some metadata from the original function:
__name__ → shows logging_w instead of fun1
__doc__ → docstring of wrapper, not original
__module__ → wrapper module
__annotations__ → argument type hints

functools.wraps(funccc) copies all the important metadata
from funccc to logging_w, so your wrapper looks more like the original function.


def wraps(original):
    def decorator(wrapper):
        wrapper.__name__ = original.__name__
        wrapper.__doc__ = original.__doc__
        wrapper.__module__ = original.__module__
        wrapper.__annotations__ = original.__annotations__
        return wrapper
    return decorator
    
"""

@logging
def fun1(t):
    for i in range(t):
        i

@logging
def fun2(t):
    while t>0:
        t -= 1

@logging
def fun3():
    time.sleep(0.1)

@logging
def fun4():
    time.sleep(1)


a = 1000000

fun1(a)
fun2(a)
fun3()

# x = 3.1415926
# print(round(x, 2))

# print(1_000*6)

print(">>>>>>>>>>>>>>>>>>>")

def decorator(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return wrapper

@decorator
def greet(name: str) -> str:
    """Say hello to someone"""
    return f"Hello, {name}"

print("With wraps:")
print("Name:", greet.__name__)
print("Doc :", greet.__doc__)
print("Annotations:", greet.__annotations__)


"""
>>>>>>>>>>>>>>>>>>>
Without wraps:
Name: wrapper
Doc : None
Annotations: {}

>>>>>>>>>>>>>>>>>>>
With wraps:
Name: greet
Doc : Say hello to someone
Annotations: {'name': <class 'str'>, 'return': <class 'str'>}
"""
print("&&&&&&&&&&&&&&&")
print("&&&&&&&&&&&&&&&")
print("&&&&&&&&&&&&&&&")

# So yes, a decorator wrapper is a special case of a closure.

# it is not a wrapper — it doesn’t “wrap another function”, it just uses captured variables.
def multiplier(x):
    # multiplier is a function that takes one argument x.
    # This x will be remembered by any inner functions defined inside multiplier.
    #          f(y) = 5 * y
    def multiply(y):
        # It uses x from the outer function.
        return x * y
        # x is captured from the outer scope. Even after multiplier
        # finishes executing, multiply still remembers the value of x
    return multiply # <=== f = multiply  # function returned by multiplier

# The outer argument x is “used up” by the closure.
f = multiplier(5) # <=== f <=== multiply(with x=5)  # function returned by multiplier
print(f"f.__closure__: {f.__closure__}")
print(f"f.__closure__[0].cell_contents: {f.__closure__[0].cell_contents:}")
"""
f = multiply
f.__closure__ = { x = 5 }  # closure captures x
"""
# multiply is returned and assigned to f.
# Even though multiplier has finished executing,
# the inner function multiply remembers x = 5.

print(f(10))  # 50
# multiply(10) → return x * y → 5 * 10 → 50

# Think of it like a locked-in environment:
# multiplier(5) → creates multiply(y) that already “knows x=5”
# # f(10) → “Ok multiply, your y=10. Multiply with your remembered x=5.”

# 😊😊😊









