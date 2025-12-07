# --- format() method ---
print("--- format() method ---")
print("a {}, {}".format(1, "mmm"))
# --- old-style % formatting ---
print("--- old-style % formatting ---")
print("Hello %s" % 10)  #0987
print("name %s" % "AAA")
name = "Alice"
age = 25
print("Hello %s, you are %d years old." % (name, age))
# Example 1: enumerate()
print("--- Example 1: enumerate() ---")
list1 = ["a", "b", "c"]
for item in list1:  # return tuples with index and item
    print(item)
print("===============")
for item in enumerate(list1):  # return tuples with index and item
    print(item)
print("===============")
tuple1 = ("c", "d", "e")
for item in enumerate(tuple1):  # return tuples with index and item
    print(item)
"""
(0, 'c')
(1, 'd')
(2, 'e')
"""
# 2️⃣ map() — apply a function to each element
print("--- map() — apply a function to each element ---")
print([item for item in range(10)])
print(map(lambda x: x ** 2, [item for item in range(10)]))
"""
A map object is an iterator — it doesn’t store all values at once.
It computes each result lazily, meaning values are generated on demand WHEN YOU ITERATE OVER IT !!!
"""
list2 = list(map(lambda x: x ** 2, [item for item in range(10)]))
print(list2)
print("------------------")
m = map(lambda x: x ** 2, range(5))
for val in m:
    print(val)
# filter
print("--- filter ---")
print(list2)
list3 = list(filter(lambda x: x % 2 == 0, list2))
print(list3)
# reduce
print("-------------")
print(type(list3))
# list3.remove(0)
list3.pop(0)
print(list3)
from functools import reduce

sum111 = reduce(lambda x, y: x * y, list3)
print(sum111)
#__repr__
print("--- __repr__ ---")


class Costam:
    def __init__(self, x: int):
        self.x = x

    def __repr__(self):
        return f"This is a specific description of x which is: {self.x}"


cosiek = Costam(2039482903482)
print(cosiek)
print(repr(cosiek))

"""
print(cosiek) calls cosiek.__str__() if available; if not, it falls back to __repr__()
"""
print("--- __repr__, __str__ not a good example ---")


class Costam2:
    def __init__(self, x: int):
        self.x = x

    def __str__(self):
        return "This is x which is {}".format(self.x)

    def __repr__(self):
        return f"This is a specific description of x which is: {self.x}"


cosiek2 = Costam2(89898989898982)
print(cosiek2)
print(repr(cosiek2))

print("--- __repr__, __str__ a GOOD example ---")


class Costam3:
    def __init__(self, x: int):
        self.x = x

    def __repr__(self):  # It’s for developers, not end users.
        return f"{self.__class__.__name__}(x={self.x})"

    def __str__(self):  # It’s meant for humans, end users, logs, and pretty-printing.
        return f"This is a specific description of x: {self.x}"


cosik3 = Costam3(777)
print(cosik3)
print(repr(cosik3))
#__dict__
import json

print("--- __dict__ ---")


class Jol:
    var1 = "var"
    sss = "sss"

    @staticmethod
    def hello():
        print("Hello")

    def __init__(self):
        self.x = 42


print(Jol.__dict__)
j1 = Jol()
print(j1.__dict__)
j1.some_attr = 123
print(j1.__dict__)
dict1 = Jol.__dict__
print(dict1)
Jol.mmm = "mmm"
dict1 = Jol.__dict__
print(dict1)
print(type(dict1))  #<class 'mappingproxy'>
dict2 = dict(Jol.__dict__)
print(dict2)
print(type(dict2))
# json_text = json.dumps(dict2, indent=4)
# print(json_text)
"""
--- Because Jol.__dict__ contains non-JSON-serializable objects:
functions (hello)
descriptors (__weakref__, __dict__)
module references
class internals
--- JSON can only handle:
str
int, float
bool
None
list, dict of the above
"""
dict2 = {key: str(value) for key, value in Jol.__dict__.items()}  #0987
json_text = json.dumps(dict2, indent=4)
print(json_text)

print("--------------------")
clean = {}
for k, v in Jol.__dict__.items():
    if isinstance(v, (str, int, float, bool, list, dict, type(None))):
        clean[k] = v

json_text = json.dumps(clean, indent=4)
print(json_text)
#abstractmethod
print("--- abstract method ---")
from abc import ABC, abstractmethod  #0987


class Abs1(ABC):
    @abstractmethod
    def sound(self):
        print("Sound method")

    @classmethod
    def sound_class(cls):
        print("Sound class method")

    @staticmethod
    def sound_static():
        print("Sound STATIC method")


class A1(Abs1):
    x: int
    y: str

    @staticmethod
    def hihi():
        print("hihi")

    # def sound(self):
    #     pass
    # TypeError: Can't instantiate abstract class A1 without an implementation for abstract method 'sound'
    def sound(self):
        # print(f"Sound from instance: {self.__annotations__}")
        #   AttributeError: 'A1' object has no attribute '__annotations__'
        # self.__class__.__annotations__
        print(f"Sound from instance: {self.__class__.__annotations__}")
        pass


aaa1 = A1()

Abs1.sound_class()
Abs1.sound_static()
aaa1.hihi()
aaa1.sound()

# 27. Demonstrate multiple inheritance and MRO (method resolution order).
print("----- multiple inheritance ------")


class AAAA:
    @staticmethod
    def pr():
        print("AAAA")


class BBBB(AAAA):
    @staticmethod
    def pr():
        print("BBBB")


class CCCC(AAAA):
    @staticmethod
    def pr():
        print("CCCC")


class DDDD(CCCC, BBBB):
    @staticmethod
    def pr():
        print("DDDD")


AAAA.pr()
BBBB.pr()
CCCC.pr()
DDDD.pr()
print("-----------------")
print(AAAA.mro())
print(BBBB.mro())
print(CCCC.mro())
print(DDDD.mro())
print("-----------------")
print("----- multiple inheritance with super() ------")


class AAAA:
    @classmethod
    def pr(cls):
        print("AAAA")


class BBBB(AAAA):
    @classmethod
    def pr(cls):
        print("BBBB")
        super().pr()


class CCCC(AAAA):
    @classmethod
    def pr(cls):
        print("CCCC")
        super().pr()


class DDDD(CCCC, BBBB):
    @classmethod
    def pr(cls):
        print("DDDD")
        super().pr()


print(">>>>>")
AAAA.pr()
print(">>>>>")
BBBB.pr()
print(">>>>>")
CCCC.pr()
print(">>>>>")
DDDD.pr()
print(">>>>>")

# 28. What is duck typing in Python?
print("--- duck typing ---")


def duckduck(thing):
    print(thing)


duckduck(32)
duckduck("str")


class Car:
    def __init__(self, number):
        self.number = number

    def what_is_that(self):
        print(f"It is a machine number: {self.number}")
        return "finish Car"


class Plain:
    def __init__(self, number):
        self.number = number

    def what_is_that(self):
        print(f"It is a machine number: {self.number}")
        return "finish Plain"


def introduce_machine(anything):
    anything.what_is_that()  # Works for anything that has a what_is_that() method #0987


print("=========================")
ccc111 = Car(90808)
ppp111 = Plain(34243)
print("=========================")
print(ccc111.what_is_that())
print(ppp111.what_is_that())
print("=========================")
introduce_machine(ccc111)
introduce_machine(ppp111)
print("=========================")

# 29. Implement operator overloading (e.g., __add__).
print("--- operator overloading ---")


class New:
    zzz = 5
    @classmethod
    def __add__(cls, other):
        print(f"Adding {New.zzz} to {other}")
        return New.zzz + other

print(New.zzz.__add__(3))
"""
New.zzz is the integer 5.
New.zzz.__add__(3) is the same as 5.__add__(3).
That calls int’s __add__, not your classmethod on New.
5.__add__(3) returns 8.
"""
print("--------------------------------")
class New111:
    def __init__(self, x):
        self.x = x

    def __add__(self, y):
        print(f"Adding {self.x} to {y} is : {self.x+y}")

nnn111 = New111(3)
nnn111 + 8
nnn111.__add__(10)
New111(4) + 12
New111(2112).__add__(2321)
# 5.__add__(3000) # SyntaxError: invalid decimal literal
print((5).__add__(4000))
print("--------------------------------")

# 30. Create a singleton pattern using a class.
print("30 ######################")
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
print("------------------------")
print(Singleton._instance)
print("-----------s1-------------")
s1 = Singleton()
print(Singleton._instance)
print("-----------s2-------------")
s2 = Singleton()
print(Singleton._instance)
print("----------s1 s2--------------")
print(s1 is s2)
print("------------------------")

'''
class Singleton(object):
    ...
Zwraca delegat umożliwiający wywołanie metody z klasy nadrzędnej
Czyli:
super().__new__ → wskazuje na object.__new__
super().__new__(cls) → tworzy instancję klasy cls przy użyciu standardowego mechanizmu

cls._instance = object.__new__(cls)
jest równoważne:
cls._instance = super().__new__(cls)

---------------

super().__new__(cls):
wywołuje konstruktor z klasy bazowej (object)
tworzy nową instancję klasy
pozwala Ci przejąć kontrolę nad liczbą instancji
jest kluczowe dla wzorca Singleton w Pythonie
'''
# singleton pattern with decorator
