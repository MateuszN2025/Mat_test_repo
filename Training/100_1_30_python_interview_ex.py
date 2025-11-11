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
# reduce
#__repr__
#__dict__
#abstartmethod
# 27. Demonstrate multiple inheritance and MRO (method resolution order).
# 28. What is duck typing in Python?
# 29. Implement operator overloading (e.g., __add__).
# 30. Create a singleton pattern using a class.
# singleton pattern with decorator

