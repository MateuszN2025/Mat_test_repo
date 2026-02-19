import inspect, math, json

def fun_hi():
    pass

# print(dir(list))
# print(help(list))
list1 = [3,4,4]
print("-----------------")
print(len(list1))
print("-----------------")
# print(inspect.getfile(list()))
# dir - Shows attributes, methods, classes, etc.
print(dir(math))
print("-----------------")
print(dir(math.sqrt.__doc__))
print("-----------------")
print(dir(math.sqrt))
print("-----------------")
print(math.sqrt.__ge__)
print("-----------------")
print(type(math.sqrt(4)))
print(math.sqrt(1))
print("-----------------")
# help(math)
print("-----------------")
print(math.sqrt.__doc__)
print("-----------------")
print(inspect.getfile.__doc__)
print("-----------------")
print(inspect.getfile(fun_hi))
print(inspect.getsource(fun_hi))
print("-----------------")
print(inspect.signature(math.pow))
print("-----------------")
print(json.__file__) # Shows where the module is located on disk.
# C:\Users\mniedziolka\AppData\Local\Programs\Python\Python39\lib\json\__init__.py
print("-----------------")
functions = inspect.getmembers(math, inspect.isfunction)
print(functions)
print("-----------------")
obj = "hello"
print(dir(obj))
'''
obj.__add__("yyy") creates a new string
It does NOT modify obj
'''
obj.__add__("yyy")
'''
That means:
You cannot change the original string
__add__ returns a NEW string
The original stays the same
'''
print(obj) # hello
obj = obj.__add__("yyy")
print(obj)
print("===========")
a = 3
a.__add__(4)
print(type(a))
print(a)
b = a.__add__(4)
print(b)
print(">>>>>>>>>>>")
print(dir(math))
print("-----------------")
print(help(math.sqrt))
print("-----------------")
print(dir(math.sqrt))
print("------- __doc__ ----------")
print(math.sqrt.__doc__)
print("-----------------")
help(math.sin)
'''
dir()	List attributes
help()	Show documentation
__doc__	Access docstring
type()	Identify object type
inspect	Deep inspection
__file__	Find module location
'''
print("-----------------")
print(list.append.__doc__)
print("-----------------")
print(list.append.__file__)
print("-----------------")
