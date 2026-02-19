# ===========================
# PYTHON QUICK MEMORY LIST
# ===========================

# 1. Basics
# ---------
x = 10          # int
y = 3.14        # float
name = "Alice"  # string
is_ok = True    # bool
nums = [1, 2, 3]  # list
tup = (1, 2, 3)   # tuple (immutable)
s = {1, 2, 3}     # set (unique items)
d = {"a": 1, "b": 2}  # dict (key-value)

# 2. Control Flow
# ---------------
if x > 5:
    print("Big")
elif x == 5:
    print("Equal")
else:
    print("Small")

for n in nums:
    print(n)

while x > 0:
    x -= 1

# 3. Functions
# ------------
def add(a, b=0):
    return a + b

# Lambda
square = lambda n: n**2

# 4. Exceptions
# --------------
try:
    val = 1 / 0
except ZeroDivisionError as e:
    print("Error:", e)
finally:
    print("Done")

# 5. File Handling
# ----------------
with open("file.txt", "r") as f:
    data = f.read()

# 6. OOP
# -------
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "Woof!"

dog = Dog("Rex")

# 7. Modules & Imports
# --------------------
import math
print(math.sqrt(16))

from datetime import datetime
print(datetime.now())

# 8. Comprehensions
# -----------------
squares = [n**2 for n in range(5)]
even_nums = {n for n in range(10) if n % 2 == 0}
dict_map = {n: n**2 for n in range(5)}

# 9. Itertools & Generators
# --------------------------
def gen():
    for i in range(3):
        yield i

import itertools
pairs = list(itertools.combinations([1,2,3], 2))

# 10. Testing (Pytest-style)
# --------------------------
def test_add():
    assert add(2, 3) == 5