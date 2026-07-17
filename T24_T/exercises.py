# ============================================================
# Pre-interview practice — Python for Test Automation + OOP/SOLID/KISS/DRY
# Job offer focus points:
#   - Practical experience in test automation using Python
#   - Decent grasp of OOP / SOLID / KISS / DRY concepts
#
# Rules:
#   - No solutions here on purpose — write your own code below each task.
#   - Keep it short. If a solution takes >15-20 lines, you're overengineering it.
#   - Time yourself: aim for 5-10 min per exercise, this is interview prep, not a project.
# ============================================================


# ------------------------------------------------------------
# SECTION 1: Python basics you must be fluent in for automation
# ------------------------------------------------------------

# Exercise 1.1
# Write a function `is_valid_status_code(code)` that returns True if `code`
# is an int between 200 and 599 (inclusive), False otherwise (including
# non-int input). This mimics validating an HTTP response in a test.

def is_valid_status_code(code) -> bool:
    # if isinstance(code, int):
    # if type(code) is int:  # excludes bool, since type(True) is bool, not int
    #         return 200 <= code <= 599       
    # else:
    #     return False
    
    result = True if type(code) is int and 200 <= code <= 599 else False
    return result
    
    # return type(code) is int and 200 <= code <= 599
    

assert is_valid_status_code(199) == False
assert is_valid_status_code(200) == True
assert is_valid_status_code("a") == False
print("------------------------------------------")
c = 1
# ternary expression — used when you want to assign one of two VALUES
a = "Nice" if c == 1 else "Bad"
print(a)
         


# Exercise 1.2
# You have a list of API response dicts, e.g.:
#   responses = [{"status": 200}, {"status": 404}, {"status": 500}]
# Write a one-liner (list comprehension) that returns only the status codes
# that are >= 400 (i.e. "failed" responses).
print("------------------------------------------")
responses = [{"status": 200}, {"status": 404}, {"status": 500}]
print([sts["status"] for sts in responses if sts["status"] >= 400])


# Exercise 1.3
# Write a function `retry(func, attempts=3)` that calls `func()` and retries
# it up to `attempts` times if it raises an exception, re-raising the last
# exception if all attempts fail. (Classic flaky-test-helper pattern.)
print("------------------------------------------")
def retry(func, attempts=3):
    last_exception = None
    for attempt in range(attempts):
        try:
            return func()
        except Exception as e:
            last_exception = e
    raise last_exception

print([_ for _ in range(3)])
print([_ for _ in range(1,3)])

# Exercise 1.4
# Given a dict of test results like:
#   results = {"test_login": "passed", "test_logout": "failed", "test_signup": "passed"}
# Write code (no imports) that prints a short summary: how many passed,
# how many failed, and the pass rate as a percentage.
print("------------------------------------------")
results = {"test_login": "passed", "test_logout": "failed", "test_signup": "passed"}

def report_summary(results: dict) -> float:
    cp, cf = 0, 0
    for v in results.values():
        if v == "passed":
            cp += 1
        else:
            cf += 1
            
    try:        
        # cp + cf == len(results)
        # pass_rate = cp/(cp+cf)*100
        pass_rate = cp/(len(results))*100
    except ZeroDivisionError as e:
        print(e)
    
    print("--- TEST RESULTS ---")
    print(f"How many passed : {cp}")
    print(f"How many failed : {cf}")
    print(f"Pass rate as a percentage: {pass_rate:.0f}%")
    
    return pass_rate
    
def report_summary2(results: dict) -> float:
    total = len(results)
    if total == 0:
        print("--- TEST RESULTS ---")
        print("No tests were run.")
        return 0.0

    passed = sum(1 for v in results.values() if v == "passed")
    failed = total - passed
    pass_rate = passed / total * 100

    print("--- TEST RESULTS ---")
    print(f"How many passed : {passed}")
    print(f"How many failed : {failed}")
    print(f"Pass rate as a percentage: {pass_rate:.0f}%")

    return pass_rate

report_summary2(results)

print("------------------------------------------")

print(len(results))

# ------------------------------------------------------------
# SECTION 2: pytest-style thinking (no pytest needed to answer)
# ------------------------------------------------------------

# Exercise 2.1
# You need to test the same function with 5 different input/expected pairs.
# Without writing 5 separate test functions, describe (in a comment) how you'd
# structure this using pytest, then write the plain-Python equivalent loop
# that asserts each pair.
import pytest

# In pytest, use one test function and feed multiple input/expected sets
# via @pytest.mark.parametrize, so each case is reported separately.
@pytest.mark.parametrize(["a", "b", "result"],
                         ((1, 2, 3),
                          (2, 3, 5),
                          (4, 5, 9),
                          (6, 7, 13),
                          (8, 9, 17)))
def test_1(a, b, result):
    assert a + b == result

# Plain-Python equivalent (no pytest):
cases = [(1, 2, 3), (2, 3, 5), (4, 5, 9), (6, 7, 13), (8, 9, 17)]
for a, b, result in cases:
    assert a + b == result


# Exercise 2.2
# Explain in a short comment: what is a pytest fixture, and why would you use
# one instead of just creating an object at the top of every test function?
# Then sketch (as a comment or pseudo-code, no need to run pytest) what a
# fixture for "a logged-in test user" might look like.

# A fixture is reusable setup/teardown code for tests.
# Use it to avoid duplication, keep tests cleaner, and control lifecycle
# (function/module/session) in one place.

@pytest.fixture(scope="session")
def logged_in_user():
    # pseudo-login: create a user/session object once per test session
    user = {"username": "qa_user", "token": "fake-token"}
    print("Logging in", user["username"])
    yield user
    print("Logging out", user["username"])


def test_verify_user(logged_in_user):
    assert logged_in_user["token"]


def test_verify_admin(logged_in_user):
    assert logged_in_user["username"] == "qa_user"
    


# ------------------------------------------------------------
# SECTION 3: OOP fundamentals
# ------------------------------------------------------------

# Exercise 3.1
# Create a class `TestCase` with attributes: name, status ("passed"/"failed"/
# "skipped"), and duration_seconds. Add a method `is_slow(threshold=2.0)` that
# returns True if duration_seconds exceeds the threshold.
print("------------------------------------------")
class TestCase:
    def __init__(self, name: str, status: str, duration_seconds: float) -> None:
        self.name = name
        self.status = status
        self.duration_seconds = duration_seconds
        
        if status in ("passed", "failed", "skipped"):
            pass
        else:
            raise ValueError("Wrong status.")
        
    def is_slow(self, threshold: float =2.0) -> bool:
        return self.duration_seconds > threshold
        
    def __str__(self) -> str:
        return f"Name: {self.name}, \
                status: {self.status}, \
                duration: {self.duration_seconds}, \
                is slow ?: {self.is_slow()}"

t1 = TestCase("name1", "passed", 1.5)
t2 = TestCase("name1", "failed", 2.5)
t3 = TestCase("name1", "skipped", 2.5)

try:
    t4 = TestCase("name1", "l", 2.5)
except ValueError as e:
    print(e)

print(t1)
print(t2)
print(t3)     


# Exercise 3.2
# Create a class `TestSuite` that holds a list of `TestCase` objects (from 3.1)
# and has a method `pass_rate()` returning the percentage of passed tests.
# This is basic composition: a TestSuite "has-a" list of TestCase.
print("------------------------------------------")
class TestSuite:
    def __init__(self, test_cases: list[TestCase]) -> None:
        self.test_cases = test_cases

    def pass_rate(self) -> float:
        if not self.test_cases:
            return 0.0
        passed = sum(1 for t in self.test_cases if t.status == "passed")
        return passed / len(self.test_cases) * 100

ts = TestSuite([t1, t2, t3])
print(f"{ts.pass_rate():.2f} %")


# Exercise 3.3
# Create two classes, `ApiTest` and `UiTest`, both inheriting from a common
# base class `BaseTest` that has a method `setup()` and `teardown()` (can just
# print something for now). Override `setup()` differently in each subclass.
# This demonstrates inheritance + polymorphism.


# ------------------------------------------------------------
# SECTION 4: SOLID principles (short, practical, testing-flavored)
# ------------------------------------------------------------

# Exercise 4.1 — Single Responsibility Principle (SRP)
# Below is a *description* of a bad class (don't write it — refactor it in
# your head/on paper first, then code the fixed version):
#   class TestRunner:
#       - reads test cases from a file
#       - executes the tests
#       - formats results as HTML
#       - sends the report by email
# Split this into separate classes, each with ONE responsibility. Just write
# the class names + one method each (skeleton only, bodies can be `pass`).


# Exercise 4.2 — Open/Closed Principle (OCP)
# You have a function that generates a report in different formats:
#   def generate_report(data, format):
#       if format == "json": ...
#       elif format == "html": ...
#       elif format == "xml": ...
# Every new format requires editing this function. Redesign it (using classes
# or a dict of functions) so adding a new format doesn't require modifying
# existing code — only adding new code.


# Exercise 4.3 — Liskov Substitution Principle (LSP)
# You have a base class `TestReporter` with a method `report(results)`.
# Write two subclasses `ConsoleReporter` and `JsonReporter`. Make sure both
# can be used interchangeably wherever `TestReporter` is expected — i.e. same
# method signature, no subclass-specific surprises (like raising errors the
# base class never raises).


# Exercise 4.4 — Interface Segregation Principle (ISP)
# Instead of one fat base class `Test` with methods `run_ui()`, `run_api()`,
# `run_performance()` that every subclass must implement (even if unused),
# split it into smaller, focused base classes/mixins. Sketch the class names
# and which mixins an `ApiTest` class would actually use.


# Exercise 4.5 — Dependency Inversion Principle (DIP)
# You have a class `TestRunner` that directly creates a `MySQLLogger()` inside
# its __init__. Refactor so `TestRunner` depends on an abstract `Logger`
# interface passed in from outside (constructor injection), so you could swap
# in a `FileLogger` or `ConsoleLogger` without touching `TestRunner`.


# ------------------------------------------------------------
# SECTION 5: KISS & DRY in practice
# ------------------------------------------------------------

# Exercise 5.1 — DRY
# Below is a description of duplicated code (don't copy it, just fix the idea):
#   test_login() builds a request payload, sends it, checks status == 200
#   test_signup() builds a (different) payload, sends it, checks status == 200
#   test_reset_password() builds a payload, sends it, checks status == 200
# Design one small helper function that removes the duplication of
# "send request + assert status" across all three tests.


# Exercise 5.2 — KISS
# You wrote a function that checks if a test name matches a naming convention
# using a complicated nested regex with lookaheads. Rewrite the requirement
# in plain English, then implement the simplest possible version using
# basic string methods (e.g. str.startswith, str.split) instead of regex,
# if the rule is simple enough to allow it.


# Exercise 5.3 — KISS vs over-engineering
# In one or two sentences (as a comment), explain when adding an abstract
# base class / plugin system for test reporters would be KISS-violating
# over-engineering for a small 3-person QA team, versus when it would be
# justified.


# ------------------------------------------------------------
# SECTION 6: Mini integration challenge (combine it all)
# ------------------------------------------------------------

# Exercise 6.1
# Design (class skeletons only, minimal bodies) a tiny test-automation
# framework with:
#   - a BaseTest class (setup/teardown)
#   - at least one subclass (e.g. ApiTest)
#   - a TestRunner that takes a list of BaseTest instances and a Logger
#     (injected, per DIP) and runs them, printing pass/fail
# Keep it under ~30 lines total. If it's growing bigger, you're violating KISS.
