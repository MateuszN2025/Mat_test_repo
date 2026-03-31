def deco(f):
    def wrapper():
        print("Before")
        f()
        print("After")
    return wrapper

@deco
def f_print():
    print('Hello')

# f_print = deco(f_print) OR @deco
print("----")
f_print()
print("----")

@deco
def f_print2():
    print('MAt')

f_print2()

# Example with a context manager:
class log_block:
    def __enter__(self):
        print("before")

    def __exit__(self, exc_type, exc, tb):
        print("after")

print("============")
with log_block():
    print("hello")


# with open("data.txt") as file:
#     content = file.read()
# This is not about decorating a function.
# It is about guaranteeing cleanup of a resource after a block ends, even on exceptions.