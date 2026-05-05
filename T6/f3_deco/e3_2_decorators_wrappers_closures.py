# Exercise 1: Wrappers
# Goal:
# Create a decorator called log_test_step that wraps a function and prints:
# - "START: <function_name>"
# - the function result
# - "END: <function_name>"
#
# Requirements:
# - The wrapper must accept any positional and keyword arguments.
# - Return the original function result.
# - Use functools.wraps so the decorated function keeps its original name.
#
# Example idea:
# @log_test_step
# def open_page(page_name):
#     return f"Opening {page_name}"
#
# Expected behavior:
# open_page("login")
# START: open_page
# Opening login
# END: open_page

import json
import w_r
from functools import wraps

def log_test_step(func):
    @wraps(func)
    # *args, **kwargs -> here they mean “collect”.
    # *args collects extra positional arguments into a tuple.
    # **kwargs collects extra keyword arguments into a dictionary.  
    # 
    # some_func("login", 10, env="test", retry=True)
    # then inside wrapper:
    #   args becomes ("login", 10)
    #   kwargs becomes {"env": "test", "retry": True}
    #   
    def wrapper(*args, **kwargs):
        print(f"START: {func.__name__}")
        # In a function call
        # Here they mean UNPACK.
        # *args unpacks the tuple back into positional arguments.
        # **kwargs unpacks the dictionary back into named arguments.
        # 
        # func(*args, **kwargs)
        # is the same as:
        #   func("login", 10, env="test", retry=True)
        # #############################################
        # def f(*args, **kwargs):   # collect
        #     g(*args, **kwargs)    # unpack
        # #############################################
        result = func(*args, **kwargs)
        print(f"{result}")
        print(f"END: {func.__name__}")
        return result
    return wrapper
    
@log_test_step
def open_page(page_name):
    return f"Opening {page_name}"

# Exercise 2: Closures
# Goal:
# Write a closure called make_retry_checker that accepts max_retries.
# It should return an inner function that accepts current_retry and returns:
# - "retry allowed" if current_retry is smaller than max_retries
# - "stop" if current_retry is equal to or greater than max_retries
#
# Requirements:
# - Do not use a class.
# - The inner function must use the outer variable from the closure.
# - Test it with at least 3 different retry values.
#
# Example idea:
# retry_checker = make_retry_checker(3)
# print(retry_checker(0))
# print(retry_checker(2))
# print(retry_checker(3))

def make_retry_checker(max_retries):
    def inner_fun(current_retry):
        if current_retry < max_retries:
            result = "retry allowed"
        else:
            result = "stop"
        return result
    return inner_fun

# Exercise 3: args, kwargs
# Goal:
# Write a function called build_request_data that collects test request data.
#
# Requirements:
# - The function should accept:
#   - one required argument: endpoint
#   - any number of positional arguments in *args
#   - any number of keyword arguments in **kwargs
# - Return a dictionary with keys:
#   - "endpoint"
#   - "path_params" -> list created from args
#   - "options" -> dictionary created from kwargs
#
# Example call:
# data = build_request_data(
#     "/users",
#     101,
#     "details",
#     method="GET",
#     timeout=10,
#     auth=True,
# )
#
# Expected result:
# {
#     "endpoint": "/users",
#     "path_params": [101, "details"],
#     "options": {"method": "GET", "timeout": 10, "auth": True},
# }

# **kwargs means: COLLECT any extra named arguments into one dictionary.
# ** is syntax in the function definition
def build_request_data(endpoint: str, *args, **kwargs) -> dict:

    result = {"endpoint":endpoint, "path_params": [*args], "options": {**kwargs}}
    print("------------------------------------------")
    print(f"args: tuple: {args}")              # Shows that *args is stored as one tuple.
    print(f"*args: unpacking to list: {[*args]}")  # Expands the tuple items and builds a list from them.
    print(f"kwargs: dictionary: {kwargs}")     # Shows that **kwargs is stored as one dictionary.
    print(f"kwargs copy: {dict(kwargs)}")
    print(f"kwargs copy: {dict(**kwargs)}")      # Use this instead of **kwargs inside an f-string.
   
    print(f"type(args): {type(args)}")
    print(f"type(kwargs): {type(kwargs)}")
    
    print(kwargs)
    print({**kwargs})

    # **kwargs is an unpacking syntax, not a standalone value.
    print("------------------------------------------")
    return result

@w_r
def main():
    print("-----------------WRAPPER-------------------------")
    open_page("login")
    print("-----------------CLOUSRE-------------------------")
    # retry_checker = inner_fun with saved max_retries = 3
    retry_checker = make_retry_checker(3)
    print(retry_checker(0))
    print(retry_checker(1))
    print(retry_checker(2))
    print(retry_checker(3))
    print("-----------------ARGS,KWARGS-------------------------")
    data = build_request_data(
        "/users",
        101,
        "details",
        method="GET",
        timeout=10,
        auth=True,
    )
    # print(f"{json.dumps(data, indent=4)}")
    print("{")
    for k,v in data.items():
        print("     ",k,v)
    print("}")
main()