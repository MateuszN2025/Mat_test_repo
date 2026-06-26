import time, inspect, os, dataclasses

class A:
    a = 1

@dataclasses.dataclass
class User:
    name: str
    age: int

def funny():
    """
    funny function
    :return:
    """
    pass

class User2:
    a: str = "AAAA"

# print("-------------------User.__annotations__-----------------------")
# print(User.__annotations__)
# print("-------------------User2.__annotations__-----------------------")
# print(User2.__annotations__)
# print(User2.__annotations__.values())
# print("-------------------dir(A)-----------------------")
# print(dir(A))
# print("------------------dir(funny)------------------------")
# print(dir(funny))
# print("------------------funny.__doc__------------------------")
# print(funny.__doc__)
# print("-------------------help(time.time)-----------------------")
# # print(help(time.time))
# print("------------------inspect.getfile(funny)------------------------")
# print(inspect.getfile(funny))
# print("------------------inspect.getsource(funny)------------------------")
# print(inspect.getsource(funny))
# print("-------------------inspect.getsource(funny)-----------------------")
# print(inspect.getsource(funny))
# print("------------------os.__file__------------------------")
# print(os.__file__)

print("------------------------------------------")
print(dir(int))





