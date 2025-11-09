# ============================================================
# Python Interview Preparation – Senior Automation Tester
# Topics: Python + Pytest + Bash + Linux
# Author: [Your Name]
# ============================================================

# ==========================
# SECTION 1 – Python Basics
# ==========================

# 1. Write a Python script that prints "Hello, World!".
print("1 ###############################")
print("Hello World")
# 2. Declare variables of different data types and print their types.
print("2 ###############################")
a = 1
b = 2.3
c = "string"
d = [1, 2, 3]
e = {4, 5, 6}
f = (9, 8, 7)
g = {"a": 23, "b": 44}
table = [a, b, c, d, e, f, g]
for i in table:
    print(f"{i} is type : {type(i)}")
# 3. Explain the difference between mutable and immutable types.
print("3 ###############################")
print("Mutable types can be changed but immutable not.")
# 4. Convert a string to an integer safely (with exception handling).
print("4 ###############################")
st = "89a"
try:
    st_int = int(st)
    print(f"Converted string to int: {st_int}")
except:
    print(f"st = {st} and this string CANNOT be converted.")
else:
    print("No action. Str for the conversion is proper.")
finally:
    print("End.")
# 5. Demonstrate string formatting using f-strings, format(), and %.
print("5 ###############################")
a = 42
www = "example.com"
# --- f-string ---
print(f"a is {a}")  # modern, clean, fast
# --- format() method ---
print("Website: {}".format(www))  #0987
# --- old-style % formatting ---
print("Hello %s" % www)  #0987
# 6. Show examples of list, tuple, set, and dict creation.
print("6 ###############################")
d = [1, 2, 3]
e = {4, 5, 6}
f = (9, 8, 7)
g = {"a": 23, "b": 44}
tab1 = [d, e, f, g]
print(tab1)
# 7. Explain list comprehensions and rewrite a for-loop using one.
print("7 ###############################")
t1 = []
for item in range(10):
    if item % 3 == 0:
        t1.append(item)
print(t1)
print([item for item in range(10) if item % 3 == 0])
# 8. What is a shallow vs deep copy in Python?
print("8 ###############################")
import copy

# Original nested list
original = [[1, 2, 3], [4, 5, 6]]
# Shallow copy – only top-level list is copied
shallow = copy.copy(original)
print(f"shallow = {shallow}")
# Deep copy – all nested objects are copied too
deep = copy.deepcopy(original)
print(f"deep = {deep}")
# Modify nested element
original[0][0] = 999
print("Original:", original)
# [[999, 2, 3], [4, 5, 6]]
print("Shallow:", shallow)
# [[999, 2, 3], [4, 5, 6]]  -> affected!
print("Deep:", deep)
# [[1, 2, 3], [4, 5, 6]]    -> unaffected
original[1] = 1000
print("Original:", original)
# Original: [[999, 2, 3], 1000]
print("Shallow:", shallow)
# Shallow: [[999, 2, 3], [4, 5, 6]]
print("Deep:", deep)
# Deep: [[1, 2, 3], [4, 5, 6]]
"""
to nadpisujesz drugi element listy głównej ([4, 5, 6] → 1000),
więc ta zmiana nie wpływa na shallow, bo shallow 
nadal trzyma referencję do starej podlisty [4, 5, 6].

original ──► [ [999, 2, 3], 1000 ]
shallow  ──► [ [999, 2, 3], [4, 5, 6] ]
deep     ──► [ [1, 2, 3],   [4, 5, 6] ]

    original[0] i shallow[0] → wskazują na ten sam obiekt
    original[1] → teraz to nowa wartość 1000, więc shallow[1] pozostało niezależne

Kluczowy wniosek:
Shallow copy kopiuje tylko "pierwszy poziom" obiektu.
Jeśli zmienisz element wewnętrzny, to zmiana jest widoczna w obu strukturach.
Jeśli jednak zamienisz cały element pierwszego poziomu, to kopia pozostaje niezależna.

shallow:
import copy
base_config = {
    "browser": "chrome",
    "timeout": 10,
    "options": ["--headless", "--disable-gpu"]
}
# Tworzymy nowy słownik, ale lista 'options' nadal wskazuje na ten sam obiekt
config_variant = copy.copy(base_config)
config_variant["browser"] = "firefox"
"""
# 9. Demonstrate unpacking of tuples and dictionaries.
print("9 ###############################")
t1 = (3, 44, 555)
t11, t12, t13 = t1
print(t11, t12, t13)

d1 = {"a": 333, "b": 9999}
d11, d12 = d1
print(d11, d12)

for k, v in d1.items():
    print(k, v)

d1 = {"a": 333, "b": 9999}

# Unpack both key–value pairs
(d11_key, d11_value), (d12_key, d12_value) = d1.items()
"""
d1.items() returns something like:
[('a', 333), ('b', 9999)]
"""
print("###############################")
print(d11_key, d11_value)
print(d12_key, d12_value)
# 10. Write code to reverse a string and a list.
print("10 ###############################")
l1 = [1, 2, 3, 4]
print(l1[::-1])
s1 = "ghj"
print(s1[::-1])
# ==========================
# SECTION 2 – Control Flow
# ==========================

# 11. Implement a simple if/elif/else example.
print(f"a is less than 10")
print("11 ###############################")
a = 10
if a > 5 and a < 10:
    print(f"a is  fron range (6,9)")
elif a < 5:
    print(f"a is less than 5")
else:
    print("other")
# 12. Demonstrate the difference between "is" and "==".
print("12 ###############################")
# Example 1: Using integers
a = 1000
b = 1000

print(a == b)  # True — they have the same value
print(a is b)  # False — they are stored at different memory locations

# Example 2: Using small integers (cached by Python)
x = 10
y = 10

print(x == y)  # True — same value
print(x is y)  # True — Python caches small integers (-5 to 256)

# Example 3: Using lists
list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(list1 == list2)  # True — they contain the same elements
print(list1 is list2)  # False — they are different objects in memory

# Example 4: Assigning one list to another
list3 = list1
print(list3 == list1)  # True — same elements
print(list3 is list1)  # True — same memory reference
"""
Explanation
== -> Compares values (content equality).
is → Compares identities (memory address or object identity).
"""
# 13. Use a for-loop to iterate through a dictionary.
print("13 ###############################")
dict = {"a": 434, "b": 789}
for item in dict:
    print(item)
for k, v in dict.items():
    print("key is %s, value is %d" % (k, v))
    print(f"key is {k}, value is {v}")

for k, v in d1.items():
    print("key is {}, value is {}".format(k, v))
# 14. Show how to use a while loop with a break condition.
print("14 ###############################")
a = 100
while (a):
    print(a)
    if a < 50:
        break
    a -= 1
# 15. Demonstrate the use of enumerate() and zip(). #0987
print("15 ############# enumerate() ##################")
# -------------------------------
# Example 1: enumerate()
# -------------------------------
fruits = ["apple", "banana", "cherry"]
print("Using enumerate():")
for index, value in enumerate(fruits):  #0987
    print(index, value)
print(enumerate(fruits))
"""
enumerate(iterable, start=0)
Adds a counter to an iterable.
Returns pairs like (index, value).
"""
print("15 ############# zip() ##################")
# -------------------------------
# Example 2: zip()
# -------------------------------
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
print("Using zip():")
for name, score in zip(names, scores):
    print(score, name)
print(zip(names, scores))
"""
zip(iter1, iter2, …)
Combines multiple iterables into tuples.
Stops when the shortest iterable is exhausted.
"""
# 16. Write a generator function using "yield".
print("16 ###############################")


def gen1():
    for jjj in range(10, 20, 2):
        yield jjj


ll22 = []
for item in gen1():
    ll22.append(item)
print(ll22)

print("16 ###############################")


def gen2():
    for jjj in range(10, 20, 3):
        yield jjj


print(list(gen2()))
# 17. Create a function that accepts variable numbers of arguments (*args, **kwargs).
print("17 ###############################")
def funn333(*args, **kwargs):
    for item_a in args:
        print(f"item_a : {item_a}")
    for item_k, item_v in kwargs.items():
        print(f"item_k : {item_k}, item_v: {item_v}")
print("============================")
funn333(1, 3, (32, 43), [989, 898, 323], a=1, b=44)
print("============================")
funn333([9999,9999,"werwer"], it=32332, dd={"aaa":"aaaa", "bbb":"bbbb"})
print("============================")
# 18. Demonstrate lambda, map(), filter(), and reduce() usage.
from functools import reduce
print("18 ###############################")
# ---------------------------------
# 1️⃣ Lambda function
print("=============lambda=====================")
# ---------------------------------
sum111 = lambda x, y: x + y
print("Lambda sum111:", sum111(45, 45))   # simple anonymous function
sf3 = lambda ii: ii ** 3
# ---------------------------------
# 2️⃣ map() — apply a function to each element
print("==============map====================")
# ---------------------------------
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, nums)) #0987
print("Squares using map():", squared)
nums3 = [111, 222, 333, 444, 555]
sr3 = list(map(sf3, nums3))
print("s3 using map():", sr3)
# ---------------------------------
# 3️⃣ filter() — keep elements that satisfy a condition
print("=============filter=====================")
# ---------------------------------
even_nums = list(filter(lambda x: x % 2 == 0, nums)) #0987
print("Even numbers using filter():", even_nums)
# ---------------------------------
# 4️⃣ reduce() — apply a function cumulatively to reduce to a single value
print("==============reduce====================")
# ---------------------------------
sum_all = reduce(lambda x, y: x + y, nums) #0987
print("Sum using reduce():", sum_all)
"""
reduce() applies the function cumulatively from left to right.
The first argument must be a function taking two parameters.
The second argument is an iterable (like a list or tuple).
"""
print("Functional Pipeline Example ###############################")
# Suppose we have a list of numbers
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Step 1: Use filter() → keep only even numbers
filtered = filter(lambda x: x % 2 == 0, nums)
# Step 2: Use map() → square each even number
mapped = map(lambda x: x ** 2, filtered)
# Step 3: Use reduce() → sum all the squared even numbers
result = reduce(lambda x, y: x + y, mapped)
print("Sum of squares of even numbers:", result)
print("==================================")
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = reduce(
    lambda x, y: x + y,
    map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, nums))
    )
print(result)
print("Functional Pipeline (List Comprehension) ###############################")
nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# One line comprehension:
result2 = sum([x ** 2 for x in nums2 if x % 2 == 0])
print("Sum of squares of even numbers:", result2)
# 19. Show how to use list comprehension with conditional logic.
print("19 ###############################")
print([item for item in range(10) if item % 2 == 0])
print([item if item % 2 == 0 else -1 for item in range(10)])
# Output: [0, -1, 2, -1, 4, -1, 6, -1, 8, -1]
# 20. Handle exceptions with try/except/finally and custom exceptions.
print("20 ###############################")
class DivisionByZeroError(Exception):
    """Custom exception for division by zero."""
    pass

a = 1
b = 0
"""
Why put ZeroDivisionError after except?
Because:
except = “catch this type of exception”
ZeroDivisionError = specific exception class you want to catch
If you don’t specify the type (just except:),
it catches all exceptions, but that’s considered
bad practice since it hides bugs you might not expect.
"""
try:
    print(a / b)
except ZeroDivisionError:
# except:
    # pass
    print("Division by 0")
    # raise DivisionByZeroError("You tried to divide by zero — not allowed!")
else:
    print("Division successful.")
finally:
    print("That's it anyway.")

print("20 ###############################")
import logging
# Configure logging
logging.basicConfig(
    filename="/home/mateusz/repo/1_app_log/app.log",             # Log file name
    # filename="1111_app.log",
    level=logging.ERROR,            # Log only errors or worse
    format="%(asctime)s - %(levelname)s - %(message)s"
)
a = 1
b = 0
try:
    print(a / b)
except ZeroDivisionError as e:
    # logging.error("Division by zero error occurred: %s", e)
    logging.error(f"Division by 0: {e}")
    print("An error occurred. Check the log file for details.")
else:
    print("Division successful.")
finally:
    print("That's it anyway.")


# ==========================
# SECTION 3 – Functions & OOP
# ==========================

# 21. Define a class with __init__, __str__, and __repr__ methods.
print("21 ###############################")
class Aaaaa:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"x is {self.x} and y is {self.y}"
    def __repr__(self):
        return f"Aaaaa({self.x}, {self.y})"
a = Aaaaa(32,43)
print(a)
# explicitly prints __repr__ #0987
print(repr(a))    # Aaaaa(32, 43)
print("==================================")
class Bbbbb:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"x is {self.x} and y is {self.y}"
b = Bbbbb(9090,7878)
print(b)
print(repr(b)) # <__main__.Bbbbb object at 0x7b9d3187a180>
# 22. Explain and demonstrate class vs instance variables.
print("22 ###############################")
class Car:
    var = 999
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def __str__(self):
        return f"Car name is {self.name} and power is {self.power} HP"
print("==================================")
print(Car.var)
print(type(Car.var))
print("==================================")
fiat = Car("tipo", 100)
print(fiat)
print(fiat.var)
print(type(fiat.var))
print("==================================")
fiat.var = 123
print(fiat.var)   # 123 (instance variable now shadows the class one)
print(Car.var)    # 999 (unchanged)
# 23. Show inheritance and method overriding.
print("23 ###############################")
class X():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    # def __str__(self):
    #     return f"a is {self.a}, b is {self.b}"
    def __str__(self):
        # return super().__str__()
        return A.__str__(self)
        """
        A.__str__(self)
        This explicitly calls the __str__ method from class A.
        It ignores the MRO and directly jumps to A.
        If you change the parent class later (or use multiple inheritance), 
        this might break or behave unexpectedly.
        """
    def fun1(self):
        print(f"Let's NOT introduce: {self.a}, {self.b}")

class A(X):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return f"a is {self.a}, b is {self.b}"
    # def fun1(self):
    #     print(f"Let's introduce: {self.a}, {self.b}")

a1 = A(2,2)
x1 = X(3,3)

print(a1)
a1.fun1()
print("==================================")
print(x1)
x1.fun1()
# 24. Demonstrate encapsulation using private attributes.
print("24 ###############################")
class team:
    var = 10
    _var = 20
    __var = 30

    def getter(cls):
        return cls.__var

t1 = team()
print(t1.var)
print(t1._var) # protected
# print(t1.__var) # error
print(t1._team__var) # workaround
print(t1.getter())
print("==================================")
# Example: Name Mangling Prevents Accidental Override
class Parent:
    def __init__(self):
        self.__secret = "Parent secret"
    def show_secret(self):
        print(self.__secret)

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__secret = "Child secret"   # looks similar, but different!

obj = Child()
obj.show_secret()
print(obj.__dict__) #0987

print("==================================")
class Parent:
    def __init__(self):
        print("Parent __init__ running")

class Child(Parent):
    def __init__(self):
        print("Child __init__ running")
        super().__init__()   # Explicitly call Parent's constructor

obj = Child()
print("==================================")
class Parent:
    def __init__(self):
        print("Parent __init__ running")

class Child(Parent):
    def __init__(self):
        print("Child __init__ running")

obj = Child()
print("==================================")
# 25. Explain and show an example of classmethod and staticmethod.
print("25 ###############################")
class Methods:
    a3 = 4
    b3 = 5
    c3 = 0
    def __init__(self):
        self.zzz = 100000000

    @classmethod
    def a_class_method(cls, self):
        c3 = cls.a3 + cls.b3
        print("This is a class method")
        print(f"a: {cls.a3} + b: {cls.b3} = c: {c3}")
        print(f"{self.zzz}") # it is not Pythonic

    @staticmethod
    def b_static_method():
        print("This is a static method")

m1 = Methods()
print("==================================")
Methods.a_class_method(m1)
Methods.b_static_method()
print("==================================")
m1.a_class_method(m1)
m1.b_static_method()
print("==================================")

'''
| Type                | Decorator       | First Parameter | Can Access            | Called via        | Typical Use                         |
| ------------------- | --------------- | --------------- | --------------------- | ----------------- | ----------------------------------- |
| **Instance method** | none            | `self`          | instance + class data | instance only     | operate on instance data            |
| **Class method**    | `@classmethod`  | `cls`           | class data only       | class or instance | factory methods, class-wide changes |
| **Static method**   | `@staticmethod` | none            | neither               | class or instance | utility/helper methods              |
'''
print("==========Pythonic===========")
class Example:
    a3 = 10
    b3 = 20

    def __init__(self):
        self.zzz = 100000000

    @classmethod
    def a_class_method(cls):
        c3 = cls.a3 + cls.b3
        print(f"This is a class method")
        print(f"a: {cls.a3} + b: {cls.b3} = c: {c3}")

    def an_instance_method(self):
        print(f"This is an instance method — zzz = {self.zzz}")

print("==================================")
obj = Example()
Example.a_class_method()
obj.an_instance_method()
print("==================================")
# 26. Create an abstract base class and subclass it.
print("26 ###############################")
from abc import ABC, abstractmethod

class Animal(ABC):  # Inherit from ABC to make it an abstract base class
    @abstractmethod
    def sound(self):
        pass
    # pass

"""
class Animal(ABC) → makes it an abstract class.
@abstractmethod → says this method must be defined in subclasses.
"""

class Dog(Animal):
    def sound(self):
        print("Bark!")


class Cat(Animal):
    def sound(self):
        print("Meow!")

dog = Dog()
# class Dog(Animal):
#   pass
# TypeError: Can't instantiate abstract class Dog without an implementation for abstract method 'sound'
cat = Cat()

dog.sound()
cat.sound()
"""
Why use abstract classes?
They’re useful when you want to:
- Enforce that all subclasses share the same structure (like an interface).
- Avoid forgetting to implement a key method.
- Create a consistent pattern in a large project.
"""
# 27. Demonstrate multiple inheritance and MRO (method resolution order).
# 28. What is duck typing in Python?
# 29. Implement operator overloading (e.g., __add__).
# 30. Create a singleton pattern using a class.

# ==========================
# SECTION 4 – Modules & Packages
# ==========================

# 31. Explain the structure of a Python package.
# 32. Demonstrate importing specific functions from a module.
# 33. Explain the difference between absolute and relative imports.
# 34. What happens when you execute a module directly vs import it?
# 35. Use __name__ == "__main__" correctly.
# 36. Write a simple script that reads configuration from a JSON file.

# ==========================
# SECTION 5 – File Handling & OS
# ==========================

# 37. Read and write to a text file.
# 38. Handle file exceptions safely.
# 39. Parse a CSV file into a list of dictionaries.
# 40. Use pathlib for file operations.
# 41. Explain context managers and create a custom one.
# 42. Use os and shutil for directory operations.
# 43. Check if a file exists, and get its size.
# 44. Write a script to search for a keyword in multiple files.
# 45. Use subprocess to run a shell command and capture output.

# ==========================
# SECTION 6 – Python Advanced Topics
# ==========================

# 46. Explain decorators and write one for logging function calls.
# 47. Explain closures and demonstrate with a nested function.
# 48. What is a generator vs iterator?
# 49. Use itertools for combinations and permutations.
# 50. Explain and demonstrate contextlib usage.
# 51. What is the GIL (Global Interpreter Lock)?
# 52. Demonstrate multithreading and multiprocessing differences.
# 53. Use asyncio to run asynchronous tasks.
# 54. Show how to use functools.lru_cache.
# 55. Explain dataclasses and create one.

# ==========================
# SECTION 7 – Testing with Pytest
# ==========================

# 56. Write a simple pytest function that tests addition.
# 57. Use pytest fixtures for setup and teardown.
# 58. Demonstrate fixture scope (function, module, session).
# 59. Explain parameterized tests with @pytest.mark.parametrize.
# 60. Mock external dependencies using unittest.mock or pytest-mock.
# 61. Use tmp_path fixture for temporary file testing.
# 62. Demonstrate pytest markers (e.g., smoke, regression).
# 63. Use pytest to test CLI scripts.
# 64. Integrate pytest with logging.
# 65. Generate and interpret pytest HTML or JUnit reports.

# ==========================
# SECTION 8 – Automation & Bash
# ==========================

# 66. Write a Python script that executes a bash command using subprocess.
# 67. Parse the output of a Linux command from Python.
# 68. Automate file cleanup using Python + Bash.
# 69. Explain how to make a Python script executable in Linux.
# 70. Demonstrate reading environment variables in Python.
# 71. Combine bash scripting and pytest runs.
# 72. Explain how to create a virtual environment and install dependencies.

# ==========================
# SECTION 9 – Testing APIs & CI/CD
# ==========================

# 73. Write a pytest test for a REST API (using requests).
# 74. Mock HTTP responses with responses library.
# 75. Explain how to organize tests in a test suite.
# 76. Demonstrate reading API test data from JSON/YAML.
# 77. Integrate pytest with CI/CD (GitHub Actions, Jenkins).
# 78. Explain pytest exit codes and how they’re used in pipelines.
# 79. Write a test that validates JSON schema.
# 80. Explain test parametrization for different environments.

# ==========================
# SECTION 10 – Linux & System-Level Scripting
# ==========================

# 81. Write a script that lists all running processes (using ps or subprocess).
# 82. Check disk space usage and alert if it exceeds a threshold.
# 83. Monitor a log file for errors using Python.
# 84. Combine Python and cron for scheduled jobs.
# 85. Explain signal handling in Python (SIGINT, SIGTERM).
# 86. Write a bash script that calls pytest and logs results.
# 87. Automate environment variable setup before tests.
# 88. Use logging and syslog integration for Linux logs.

# ==========================
# SECTION 11 – Code Quality & Best Practices
# ==========================

# 89. Explain PEP8 and use flake8/pylint for static analysis.
# 90. Use typing and type hints in functions.
# 91. Write docstrings in Google or NumPy style.
# 92. Explain dependency injection and mocking for testability.
# 93. Demonstrate how to structure a test automation project.
# 94. Explain the concept of test data management.
# 95. Discuss when to use fixtures vs setup methods.
# 96. Optimize slow pytest tests.
# 97. Integrate coverage.py and analyze results.
# 98. Use pre-commit hooks to enforce code style.

# ==========================
# SECTION 12 – Bonus: Interview Discussion Topics
# ==========================

# 99. Explain how Python memory management works (ref counting + GC).
# 100. What are your strategies for debugging and profiling Python code?
# 101. How would you design a scalable automation framework?
# 102. Compare pytest to unittest.
# 103. Describe how you ensure reliability and maintainability in tests.
# 104. Explain dependency management with requirements.txt and poetry.
# 105. Discuss integration testing vs unit testing vs E2E.
# 106. Explain CI/CD integration and how to gate merges on test results.

# ============================================================
# END OF FILE – Python Interview Review Checklist
# ============================================================
