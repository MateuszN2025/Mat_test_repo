def deco(f):
    def wrapper():
        print("Before")
        f()
        print("After")
    return wrapper

# @deco
def f_print():
    print('Hello')

f_print = deco(f_print)
f_print()

@deco
def f_print2():
    print('MAt')

f_print2()