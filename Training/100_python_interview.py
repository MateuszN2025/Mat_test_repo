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
print("Website: {}".format(www)) #0987
# --- old-style % formatting ---
print("Hello %s" % www) #0987
# 6. Show examples of list, tuple, set, and dict creation.
print("6 ###############################")
d = [1, 2, 3]
e = {4, 5, 6}
f = (9, 8, 7)
g = {"a": 23, "b": 44}
tab1 = [d,e,f,g]
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
# 10. Write code to reverse a string and a list.

# ==========================
# SECTION 2 – Control Flow
# ==========================

# 11. Implement a simple if/elif/else example.
# 12. Demonstrate the difference between "is" and "==".
# 13. Use a for-loop to iterate through a dictionary.
# 14. Show how to use a while loop with a break condition.
# 15. Demonstrate the use of enumerate() and zip().
# 16. Write a generator function using "yield".
# 17. Create a function that accepts variable numbers of arguments (*args, **kwargs).
# 18. Demonstrate lambda, map(), filter(), and reduce() usage.
# 19. Show how to use list comprehension with conditional logic.
# 20. Handle exceptions with try/except/finally and custom exceptions.

# ==========================
# SECTION 3 – Functions & OOP
# ==========================

# 21. Define a class with __init__, __str__, and __repr__ methods.
# 22. Explain and demonstrate class vs instance variables.
# 23. Show inheritance and method overriding.
# 24. Demonstrate encapsulation using private attributes.
# 25. Explain and show an example of classmethod and staticmethod.
# 26. Create an abstract base class and subclass it.
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
