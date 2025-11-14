# --- format() method ---
print("--- format() method ---")
print("a {}, {}".format(1,"mmm"))
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
for item in list1: # return tuples with index and item
    print(item)
print("===============")
for item in enumerate(list1): # return tuples with index and item
    print(item)
print("===============")
tuple1 = ("c", "d", "e")
for item in enumerate(tuple1): # return tuples with index and item
    print(item)
"""
(0, 'c')
(1, 'd')
(2, 'e')
"""
# 2️⃣ map() — apply a function to each element
print("--- map() — apply a function to each element ---")
print([item for item in range(10)])
print(map(lambda x: x**2,[item for item in range(10)]))
"""
A map object is an iterator — it doesn’t store all values at once.
It computes each result lazily, meaning values are generated on demand WHEN YOU ITERATE OVER IT !!!
"""
list2 = list(map(lambda x: x**2,[item for item in range(10)]))
print(list2)
print("------------------")
m = map(lambda x: x**2, range(5))
for val in m:
    print(val)
# filter
print("--- filter ---")
print(list2)
list3 = list(filter(lambda x: x % 2==0,list2))
print(list3)
# reduce
print("-------------")
print(type(list3))
# list3.remove(0)
list3.pop(0)
print(list3)
from functools import reduce
sum111 = reduce(lambda x,y: x*y, list3)
print(sum111)
#__repr__
print("--- __repr__ ---")
class Costam:
    def __init__(self, x:int):
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
    def __init__(self, x:int):
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

    def __repr__(self): # It’s for developers, not end users.
        return f"{self.__class__.__name__}(x={self.x})"

    def __str__(self): # It’s meant for humans, end users, logs, and pretty-printing.
        return f"This is a specific description of x: {self.x}"

cosik3 = Costam3("777")
print(cosik3)
print(repr(cosik3))
#__dict__
import json
print("--- __dict__ ---")
class Jol():
    var1 = "var"
    sss = "sss"
    def hello(self):
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
print(type(dict1)) #<class 'mappingproxy'>
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
dict2 = {key: str(value) for key, value in Jol.__dict__.items()} #0987
json_text = json.dumps(dict2, indent=4)
print(json_text)

print("--------------------")
clean = {}
for k, v in Jol.__dict__.items():
    if isinstance(v, (str, int, float, bool, list, dict, type(None))):
        clean[k] = v

json_text = json.dumps(clean, indent=4)
print(json_text)
#abstartmethod
# 27. Demonstrate multiple inheritance and MRO (method resolution order).
# 28. What is duck typing in Python?
# 29. Implement operator overloading (e.g., __add__).
# 30. Create a singleton pattern using a class.
# singleton pattern with decorator

