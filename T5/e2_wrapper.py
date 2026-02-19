def function_wrapper(func):
    def wrapper(*args, **kwargs):
        print("--------------")
        print("start")
        result = func(*args, **kwargs)
        print(result)
        print("end")
        return result
    return wrapper

@function_wrapper
def sum1(*args):
    return sum(args)

l1 = [1, 33, 44]
# print(sum1(*l1))
sum1(*l1) #unpacking the list
sum1(3,4)
print("=========")
l2 = [3,4,5,6]
print(l2)
print(*l2)






















print(">>>>>>>>>>>>>>>>>>")

def f_w(func1):
    def wrap(v,u):
        print("xxx")
        return func1(v,u)
    return wrap

@f_w
def f_1(x,y):
    print("hi")

@f_w
def f_2(x,y):
    return print(x+y)

f_1(2222,5555)
# xxx
# hi

f_2(3,4)
# xxx
# 7

print(">>>>>>>>>>>>>>>>>>")
def fw(func2):
    def wrap_f(*args):
        print("wrap is working")
        # return print(func2(*args))
        # print() always returns None
        result = func2(*args)
        print("result:", result)
        # return result
    return wrap_f

'''
🔹 Visualizing the Flow
Original function: func2
Decorator: fw(func2) -> returns wrap_f
Calling decorated function: f222(3, 4) -> actually calls wrap_f(3,4)
Inside wrap_f: calls func2(3,4) -> returns result
wrap_f returns result -> caller receives result
'''

# l333 = list(range(10))

@fw
def f111():
    print("anything")
    # return None

@fw
def f222(xx,yy):
    # return print(sum([xx, yy]))
    # print() always returns None
    return sum([xx, yy])

f111()
# wrap is working
# anything
# result: None

f222(55,55)
# wrap is working
# result: 110

print("-----------")
rrr = f222(656,656)
#  it is fine because we have in decorator: return result

















