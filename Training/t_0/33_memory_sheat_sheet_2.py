"""
===========================================
      PYTHON CHEAT SHEET + STUDY PATH
===========================================

📌 STUDY PATH CHECKLIST

1. Fundamentals
   - [ ] Data types (int, float, str, bool, list, tuple, set, dict)
   - [ ] Variables & operators
   - [ ] Control flow (if, for, while, break/continue)

2. Functions & Modules
   - [ ] Defining functions, default args
   - [ ] *args / **kwargs !
   - [ ] Lambda functions
   - [ ] Imports & built-in modules (math, datetime, os, sys)

3. Error Handling
   - [ ] try/except/finally
   - [ ] Common exceptions
   - [ ] Custom exceptions

4. File & OS Handling
   - [ ] Open/read/write files
   - [ ] Context managers (with)
   - [ ] Working with os / pathlib

5. Object-Oriented Programming
   - [ ] Classes & objects !
   - [ ] Inheritance, polymorphism !
   - [ ] Dunder methods (__init__, __str__)
   - [ ] Encapsulation (private/protected/public)

6. Data Structures & Iteration
   - [ ] List/dict/set comprehensions
   - [ ] Generators & yield
   - [ ] Itertools basics

7. Testing & QA
   - [ ] Unit testing with pytest
   - [ ] Fixtures, parametrization
   - [ ] Mocking & assertions
   - [ ] Test automation workflows

8. Advanced Topics
   - [ ] Decorators & context managers
   - [ ] Virtual environments & pip
   - [ ] Logging
   - [ ] Type hints (typing)

9. Automation & Tools
   - [ ] CI/CD with Jenkins/GitHub Actions
   - [ ] Linting (flake8, black, pylint)
   - [ ] Packaging (setup.py, pyproject.toml)

10. Extras for Embedded/QA
   - [ ] Linux + Shell scripting integration
   - [ ] Working with APIs (requests)
   - [ ] Parsing data (JSON, XML, CSV)
   - [ ] Performance testing & profiling
"""

# ==== PYTHON QUICK RECALL ====

# 1. Basics
x=1; y=3.14; s="hi"; b=True
lst=[1,2,3]; tup=(1,2); st={1,2}; d={"a":1}

# 2. Control
if x>0: print("pos")
for i in lst: print(i)
while x>0: x-=1

# 3. Functions
def f(a,b=0): return a+b
g = lambda n: n**2

# 4. Exceptions
try: 1/0
except ZeroDivisionError: print("err")

# 5. File I/O
with open("f.txt","r") as f: data=f.read()

# 6. Classes
class A:
    def __init__(s,n): s.n=n
    def show(s): return s.n
class B(A): pass

# 7. Imports
import math; from datetime import datetime

# 8. Comprehensions
sq=[n**2 for n in range(5)]
ev={n for n in range(10) if n%2==0}
m={n:n**2 for n in range(5)}

# 9. Generators
def gen():
    for i in range(3): yield i

# 10. Testing (pytest)
def test_f(): assert f(2,3)==5
