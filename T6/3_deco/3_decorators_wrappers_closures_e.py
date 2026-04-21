# def f1(func1):
#     def w_f1():
#         print("in wrapper")
#         func1()
#         print("out wrapper")
#     return w_f1
#
# @f1
# def hello():
#     print("hello")
#
# def something():
#     print("something")
#
# print("----")
# hello()
# print("----")
# something()
# print("----")
# something = f1(something)
# something()



# def f2(func2):
#     def w_f2(a, b):
#         print(f"--- {func2.__name__} ---")
#         result = func2(a, b)
#         return result
#     return w_f2
#
# @f2
# def name1_sum(a, b):
#     return a + b
#
# @f2
# def name2_multiplay(a, b):
#     return a * b
#
# print(name1_sum(1,4))
# print(name2_multiplay(5,7))

# # does not modify future calls.
# def f2(func):
#     print("start")
#     func()
#     print("stop")
#     return func
#
#
# # def f2(func):
# #     def w_f2(*args):
# #         print("-----")
# #         print(args)
# #         result = func(*args)
# #         return result
# #     return w_f2
#
# # To actually change behavior, you need to return a new function.
# # Take a function, return a new enhanced function.
#
#
# @f2
# def sumik(*args):
#     return sum(args)
#
# # sumik = f2(sumik)
#
# print(sumik(1,2))
# print(sumik(1,2,3))
# print(sumik(1,2,3,4))




def f3(func3):
    def w_f3(*args, **kwargs): # In function definitions → to collect/pack arguments
        print(f"---- {func3.__name__} ----")
        print(f"args: {args}")
        print(f"kwargs: {kwargs}")
        result = func3(*args, **kwargs) # In function calls → to unpack/spread arguments
        print(result)
        return result
    return w_f3

@f3
def sum1(a, b):
    return a + b

@f3
def sum2(a, b, c):
    return a + b + c

@f3
def sum3(list1):
    return sum(list1)

# print(sum1(3,4))
# print(sum2(3,4,5))
# print(sum3([9,9,9,9]))
sum1(3,4)
sum2(3,4,5)
sum3([9,9,9,9])


"""
* and **

Think of them as packing and unpacking tools
They’re used in two main places:

In function definitions → to collect/pack arguments
In function calls → to unpack/spread arguments
"""
print("=================")
list3 = [1,2,3,4]
print(list3)
print(*list3)
z, x, c, v = list3
print(z, x, c, v)


dict3 = {"a":111, "b": 222}
print(f"dict3:{dict3}")
print(f"*dict3:", *dict3) # *dict3 means: iterate over keys
# print(f"**dict3:", **dict3) # ERROR TypeError: 'a' is an invalid keyword argument for print()


def atest(cc, dd): # *dict3  →  "aa", "bb"
    # cc = "aa"
    # dd = "bb"
    # f(c="a", d="b")   ❌ WRONG interpretation
    # f("a", "b")       ✅ CORRECT interpretation
    print("========= atest ========")
    print(cc, dd)
    print(type(cc))


def atest2(cc, dd): # f(**dict3) -> f(cc=111, dd=222)
    print("========= atest 2 ========")
    print(cc, dd)
    print(type(cc))
    print(sum([cc, dd]))
    print(cc + dd)

def atest3(**kwargs): # f(**dict3) -> f(cc=111, dd=222)
    print("========= atest 3 ========")
    print(kwargs)
    print(kwargs.values())
    print(*kwargs.values())



dict3 = {"aa": 111, "bb": 222}
atest(*dict3)

dict3 = {"cc": 111, "dd": 222}
atest2(**dict3)

dict3 = {"aa": 111, "bb": 222}
atest3(**dict3)

# atest2(aa=111, bb=222)
# atest2(**dict3)
# TypeError: atest2() got an unexpected keyword argument 'aa'
# dict3 = {"cc": 111, "dd": 222}
# atest2(cc=111, dd=222)



"""More precise version:
*dict → gives keys only (when iterating a dict)
**dict → gives key=value pairs (used for keyword arguments)"""

print("=================")
# print(sum(1,2)) #TypeError: 'int' object is not iterable

# IMPORTANT CONCEPT
# * vs **
# Symbol	Meaning	Expands into
# *dict	unpack keys	positional arguments
# **dict	unpack key-value pairs	keyword arguments


# func(*items)        # unpack into function args
# [*items]            # unpack into list
# a, *b = seq         # unpack assignment



print(">>>>>>>>")
dict11 = {"lll":333, "ppp": 999}
print([*dict11.values()])





print("####################")

def abc(x1):
    def xyz(y1):
        return x1 + y1
    return xyz

# abc(x1) is an outer function that takes a value x1.
# Inside it, you define another function xyz(y1).
# xyz uses both:
# its own argument y1
# the outer variable x1
# abc returns the function xyz (not the result of calling it).
# Python keeps x1 in the function’s enclosing scope, so xyz can still access it later.
# A closure is like:
# A function + its saved environment (memory)


f = abc(7) # <=== xyz
# x1 = 7
print(f(8)) # x1 is remembered in xyz(8)


"""
Closures are useful when you want to:
    pre-fill some values
    reuse customized behavior
    avoid repeating parameters again and again
"""


print("______-----_________-----_______")
def discounter(discount):
    discount1 = (100 - discount)/100
    def pricer(price):
        return f"${price * discount1:.2f} because of {discount}% of discount"
    return pricer



price_with_20_off = discounter(20) # 'price_with_discount' becomes 'pricer'
# Instead of passing discount every time:
#   apply_discount(price, discount)
#   price_with_20_off(price)
# A closure lets you pre-configure a function with hidden parameters and reuse it cleanly.
print(price_with_20_off(100))
print(price_with_20_off(90))
print(price_with_20_off(80))
print("---")
price_with_30_off = discounter(30)
print(price_with_30_off(100))
print(price_with_30_off(90))
print(price_with_30_off(80))


# def x_fun(z1):
#     def y_fun(m1):
#         return z1 + m1
#     return y_fun
#
# xxx = x_fun(9)
# print(xxx(10))

print("______-----_________-----_______")
def discounter1(func):
    def w_pricer1(price):
        result = func(price)
        result1 = (100 - result) / 100
        return f"Initial price ${price} and after {result}% of discount : ${price * result1:.2f}"
    return w_pricer1

# def discounter1(func):
#     def wrapper(price):
#         discount = func(price)
#         final_price = price * (1 - discount / 100)
#         return f"${final_price:.2f} because of {discount}% discount"
#     return wrapper

@discounter1
def discount_20(price):
    return 20

@discounter1
def discount_40(price):
    return 40


print(discount_20(100))
print(discount_40(100))




