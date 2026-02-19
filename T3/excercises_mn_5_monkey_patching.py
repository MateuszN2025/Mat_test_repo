import math
import requests

print("monkey patching")

print(math.sqrt(4))

def anything(a):
    return "anything"

math.sqrt = anything # Patching

print(math.sqrt(2))

print("============")
def fake_get():
    return "Fake Response"

requests.get = fake_get # Patching
print(requests.get)
print(requests.get())


class Car:
    pass

def hello():
    return "hello"

Car.hello = hello # Patching

ccc = Car()
print(">>>>>>>> 1 >>>>>>>>>")
print(Car.hello())
print(">>>>>>>> 2 >>>>>>>>>")
print(ccc.hello)
# print(ccc.hello())
# TypeError: hello() takes 0 positional arguments but 1 was given
# (self was given as an object instance)

print(">>>>>>>> 3 >>>>>>>>>")
ccc.hello = hello
print(ccc.hello)
print(ccc.hello())

"""
🔥 Advantages
Quick fixes
Useful for testing
Flexible and powerful
No need to modify original code

⚠️ Disadvantages
Makes code harder to understand
Can break unexpectedly
Debugging becomes difficult
Not recommended in production unless necessary

🎯 Interview Definition (Short)
Monkey patching is dynamically modifying or extending
a class or module at runtime without altering its original source code.
"""