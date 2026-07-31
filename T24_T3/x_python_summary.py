print("---------------dicts---------------------------")
dict1 = {"a": 1, "b": 2}
dict2 = {}
for k, v in dict1.items():
    dict2[v] = k
print(dict2)
# Reverse a dictionary
print({k1: v1 for k1, v1 in dict1.items()})
print({v2: k2 for k2, v2 in dict1.items()})
print([item for item in range(10) if item % 2 == 0])

dict3 = dict1
print(id(dict1))
print(id(dict3))
print(dict3 is dict1)

dict4 = {"c": 3, "d": 4}
# Merge two dictionaries.
dict1.update(dict4)
print(dict1)
print(dict1["c"])
dict1["c"] = 888
print(dict1)
dict1.pop("d")
print(dict1)
print(dict1.get("c", 0))
dict5 = {"e": 5, "f": 6}
# Merge two dictionaries.
print({**dict1, **dict5})
print("---------------lists---------------------------")
list1 = [1,2,3,4,5]
print(list1[0])
list1[1] = 777
print(list1[1])
print(list1[:4])

# Group a list of objects.
items = [
    {"name": "Apple", "type": "fruit"},
    {"name": "Banana", "type": "fruit"},
    {"name": "Carrot", "type": "vegetable"},
    {"name": "Broccoli", "type": "vegetable"},
]

fruit_list = []
for i in items:
    if i["type"] == "fruit":
        fruit_list.append(i["name"])
        
print("fruit_list", fruit_list)
print("vegetable_list", [v["name"] for v in items if v["type"] == "vegetable"])

# Find duplicate values.
list_of_duplicates = []
list2 = [1, 2, 3, 2, 4, 1]
for i in list2:
    if not i in list_of_duplicates and list2.count(i) > 1:
        list_of_duplicates.append(i)        
print(list_of_duplicates)

# Find duplicate values. map
s1 = lambda l : sum(l)
print(s1(list2))

s2 = lambda x : x**3
print(list(map(s2, list2)))

print("------------------JSON------------------------")
# Parse a JSON response.
# input:'{"name":"Alice","age":30}'
# output:{"name": "Alice", "age": 30}
json_str = '{"name":"Alice","age":30}'
import json
python_dict = json.loads(json_str)
print(python_dict)

json_str2 = json.dumps(python_dict, indent=4)
print(json_str2)
print(type(json_str2))

# Function	Use case
# json.dumps() object Python → JSON (string)
# json.dump()  object Python → file with JSON

# json.loads() JSON string → object Python
# json.load()  JSON file   → object Python

print("------------------func, wrapers, decorators------------------------")

def fun_wrap(func):
    def wrapper(*args, **kwargs):
        print("🔵")
        result = func(*args, **kwargs)
        print("🟡")
        return result
    return wrapper

@fun_wrap
def hiover(text: str) -> int:
    print(text)
    return len(text)

hiover("opreopre")
print(hiover("eeww"))

# @my_decorator
# greet = my_decorator(greet)

print("------------------classes------------------------")

class Machine:
    def __init__(self, size, weight, speed, rating):
        self.size = size
        self.weight = weight
        self.speed = speed
        self.rating = rating
        
    def __str__(self):
        return f"Size:{self.size}cm, weight:{self.weight}kg, speed:{self.speed}km/h "
    
    def display_rating(self, symbol: str):
        result = ""
        for _ in range(self.rating):
            result += symbol        
        print(f"Rating:{result}")
            

class Car(Machine):
    def __init__(self, size, weight, speed, rating, company):
        self.company = company
        super().__init__(size, weight, speed, rating)
    
    def __str__(self):
        return super().__str__() + f",company:{self.company}ℹ️"
    
c1 = Car(4000, 2000, 200, 1, "Masseratti")
print(c1)
c1.display_rating(symbol="⭐")

from dataclasses import dataclass

@dataclass
class Plane():
    company: str
    status: str
    hours_of_flight: int

p1 = Plane("Boeing", "Healthy", 32423)

print(p1)
    
from abc import ABC, abstractmethod

class Shape(ABC):
   
    @abstractmethod
    def shape(self):
        pass

@dataclass
class Circle(Shape):
    radius: int
    
    def shape(self):
        print("shape")

c1 = Circle(1)   
print(repr(c1))
    
print("------------------tuples------------------------")
t1 = (1,)
t2 = (2,3,"human", "human", "human")
a, b, c, d, e = t2
print(a)
print(t2.count("human"))
print(t1)

print("------------------sets------------------------")
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print(set1 | set2) # {1, 2, 3, 4, 5, 6, 7, 8}
print(set1 & set2) # {4, 5}
print(set1 ^ set2) # {1, 2, 3, 6, 7, 8}
print(set1 - set2)  # {1, 2, 3}
print(set2 - set1)  # {6, 7, 8}
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))    # True
print(b.issuperset(a))  # True

print("------------------exeptions------------------------")
for item in [1,2,3,0,4,5]:
    print("------------------------------------------")
    # result = 1/item
    # print(f"ℹ️  result:{result}")
    # without try except program will stop
    try:
        result = 1/item
    except Exception as e:
        print(f"⚠️ {e} {type(e).__name__}")
    else:
        print(f"ℹ️  result:{result}")
    finally:
        print("✅  Operation is done")
        
"""
Value/type issues: ValueError, TypeError
Missing keys/attrs: KeyError, AttributeError
Indexing: IndexError
Files/IO: FileNotFoundError, PermissionError, OSError
Numeric: ZeroDivisionError, OverflowError
"""


print("------------------closures------------------------")
def fun1(x):
    # param = x
    def fun2():
        y = 5
        list1 = [x, y]
        result2 = sum(list1)
        result = x + y
        return result2
    return fun2

print(fun1(10)())
print(fun1(15)())
print(fun1(20)())
a = fun1(35)
print(a())

print("------------------*args ------------------------")
def sumik(*args):
    # print(args)
    sum_list = []
    # print("------------------------------------------")
    for i in args:        
        if isinstance(i, list):
            return sum(i)
        else:
            sum_list.append(i)
    return sum(sum_list)

def sumik(*args):
    if len(args) == 1 and isinstance(args[0], list):
        return sum(args[0])
    return sum(args)

    
# sumik(1)
# sumik(1,2)
# sumik([11,22])
print(sumik(1))
print(sumik(1,2))
print(sumik([11,22]))
print("------------------------------------------")
def show(*args):
    # print(args)
    # (1,)
    # (1, 2)
    # ([11, 22],)
    # print(*args)
    # 1
    # 1 2
    # [11, 22]
    pass

show(1)
show(1,2)
show([11,22])

print("-----------------sum of a tuple-------------------------")
print(sum((1,3,4,4)))


print("------------------**kwargs ------------------------")
def keywords(**kwargs):
    # print(**kwargs)
    print(kwargs) # {'a': 1, 'b': 3}
    print(kwargs.values())
    list_from_dict = list(kwargs.values())[0]
    print(list_from_dict)
    if isinstance(list_from_dict, dict):
       print(sum([v for v in list_from_dict.values()]))
       print(sum(list(list_from_dict.values())))
    else:
        print(sum(kwargs.values()))
    
    
keywords(a=1, b=3)
keywords(x=11, y=33, z=44)
keywords(a = {'aa': 122, 'bb': 333}) # dict_values([{'aa': 122, 'bb': 333}])


print("------------------modules and packages------------------------")

# A module is any .py file. We can import whole modules or selected names.
import math
from datetime import datetime
import json as js

print("math.pi:", round(math.pi, 4))
print("now:", datetime.now().strftime("%Y-%m-%d %H:%M"))
print("alias import works:", js.dumps({"ok": True}))

# Common import styles:
# 1) import module_name
# 2) from module_name import object_name
# 3) import module_name as alias

# __name__ is "__main__" when a file is run directly.
print("current module name:", __name__)

# A package is a folder that groups related modules.
# Modern Python supports namespace packages (folder without __init__.py),
# but adding __init__.py is still common and explicit.

# Example package layout:
# my_package/
#   __init__.py
#   calc.py
#   text_utils.py
#
# Example usage:
# from my_package.calc import add
# import my_package.text_utils as tu
# print(add(2, 3))
# print(tu.slugify("Hello World"))

# Relative imports are used inside packages:
# from .calc import add
# from ..helpers.formatter import pretty

print("------------------File handling------------------------")
with open("./T24_T3/my_file.txt", "w") as f:
    f.write("Hello!\n")
    
open("./T24_T3/empty.txt", "w").close()

print("------------------Path------------------------")  
# file1 = "learning_sample.json"
from pathlib import Path

file1 = Path(__file__).resolve().parent / "learning_sample.json"

Path("my_file.txt").write_text("Hello!\n", encoding="utf-8")

# with open(file=file1, mode="w") as f:
    # python_dict = json.load(f)
    # lines_list = f.readlines()
    # lines_list = [line.rstrip("\n") for line in f]
    
    # for line in f:
        # print(line)
        
    # with open("learning_sample.json", "r") as f:
    #     for _ in range(1000):          # any upper limit
    #         line = f.readline()
    #         if line == "":             # EOF
    #             break
    #         print(line.rstrip("\n"))
    
    # f.write("asda")
    # pass
        
# print(python_dict)
# print(lines_list)

print("------------------generators------------------------")

def gen1():
    for i in range(1,10,2):
        yield i
    # yield 1
    # yield 2
    # yield 3

# Use one generator instance:
g = gen1()
print(next(g))
print(next(g))
print(next(g))

"""
def invalid_login_cases():
    # Generator: yields one test case at a time
    yield {"username": "", "password": "secret", "expected_status": 400}
    yield {"username": "qa_user", "password": "", "expected_status": 400}
    yield {"username": "wrong_user", "password": "wrong_pass", "expected_status": 401}


@pytest.mark.parametrize("case", list(invalid_login_cases()))
def test_login_negative(case):
    response = requests.post(
        "https://example.com/api/login",
        json={"username": case["username"], "password": case["password"]},
        timeout=10,
    )
    assert response.status_code == case["expected_status"]
"""


print("------------------iterators------------------------")

class Iter1:
    def __init__(self, start, stop, step):
        self.current = start
        self.stop = stop
        self.step = step
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        value = self.current
        self.current += self.step
        return value
            
i1 = Iter1(1,10,2)
print(next(i1))
print(next(i1))
print(next(i1))

print("------------------context manager with contextmanager------------------------")
from contextlib import contextmanager

@contextmanager
def open_file(path):
    f = open(file=path, mode="r")
    try:
        yield f.read()
    finally:
        f.close()
    
with open_file(file1) as f:
    print(f)
    
print("------------------context manager with class------------------------")
    
class ConMan1:
    def __init__(self, file1):
        self.file1 = file1
        self._file = None
    
    def __enter__(self):
        try:
            self._file = open(self.file1, "r")
            return self._file.read()
        except FileNotFoundError as e:
            print(e)
            raise        
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self._file:
            self._file.close()
        return False
    
cm = ConMan1(file1)
with cm as f:
    print(f)
    
    
# the easiest   
class ConMan2:
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        self.file = open(self.file_name, "r")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()  
print("------------------------------------------")
cm2 = ConMan2(file1)
with cm2 as f:
    print(f.read())
    
print("------------------ subprocess ------------------------")  
print("⚠️⚠️⚠️  vbox must be run first ⚠️⚠️⚠️")
import subprocess

# cmd = subprocess.run(
#     args=[
#         "sshpass",
#         "-p", "changeme1@",
#         "ssh",
#         "vboxuser1@192.168.0.152",
#         "ip a | grep 192",
#     ],
#     capture_output=True,
#     text=True,  # Returns strings, not bytes
#     check=False,  # Don't raise on non-zero exit
# )

# # Access both streams
# print("STDOUT:", cmd.stdout)
# print("STDERR:", cmd.stderr)
# print("Exit code:", cmd.returncode)

# Common pattern: log stderr when exit code is non-zero
# if cmd.returncode != 0: # 127 != 0 -> True -> logger.error
#     logger.error(f"Command failed: {cmd.stderr}")

    
print("------------------API------------------------")  
print("⚠️⚠️⚠️  api must be run first ⚠️⚠️⚠️")
import requests

session = requests.Session()

api_url="http://127.0.0.1:8000"
endpoint_users="/users"
endpoint_auth="/auth/token"
# token="token-admin"

import subprocess
import socket
import time

# #################################################################
def is_api_running(host="127.0.0.1", port=8000, timeout=2):
    """Check if API is listening on the port."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        result = sock.connect_ex((host, port))
        return result == 0  # 0 = success, port is in use
    finally:
        sock.close()

def start_api_if_needed():
    """Start API only if it's not already running."""
    if is_api_running():
        print("✓ API is already running on port 8000")
        return
    
    print("⚠️  API not running, starting...")
    try:
        # Use Popen to start the server in background (doesn't wait for it to finish)
        # Call the shell script directly; the alias only exists in an interactive shell.
        subprocess.Popen(
            args=["python", "-m", "uvicorn", "T18.api.api_2:api_2", "--host", "127.0.0.1", "--port", "8000"],
            # args=["bash", "/home/mniedziolka/PP/Mat_test_repo/T18/tests/r_api.sh"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        time.sleep(4)  # Give server time to start
        
        # Verify it's actually running
        if is_api_running():
            print("✓ API started successfully")
        else:
            raise RuntimeError("API failed to start - port 8000 still not listening")
    except Exception as e:
        print(f"✗ Failed to start API: {e}")
        raise

# Usage in your test setup
start_api_if_needed()

# #################################################################


data_auth = "username=admin&password=admin123"
headers_auth = {"Content-Type": "application/x-www-form-urlencoded"}
response_auth = session.post(
    url=api_url + endpoint_auth,
    data=data_auth,
    headers=headers_auth,
    timeout=10
    )

response_auth.raise_for_status()
auth_payload = response_auth.json()
print(auth_payload)

token = auth_payload.get("access_token") or auth_payload.get("token")
print("token:", token)

headers_token = {"Authorization": f"Bearer {token}"}
response_get = session.get(
    url=api_url + endpoint_users,
    headers=headers_token,
    timeout=10)
response_get.raise_for_status()
print(response_get.json())


"""
import os
from urllib.parse import urlencode, urlparse, parse_qs

api_url = os.getenv("API_URL", "http://localhost:8000")

# Method 1: Use urlencode() for query parameters (RECOMMENDED)
params = {
    "username": "qa_user",
    "status": "active",
    "limit": 10
}
endpoint = "/users"
full_url = f"{api_url}{endpoint}?{urlencode(params)}"
# Result: http://localhost:8000/users?username=qa_user&status=active&limit=10

# Method 2: requests library handles it automatically
import requests
response = requests.get(
    f"{api_url}/users",
    params=params,  # Automatically encoded with ? and &
    timeout=10
)

# Method 3: Manual string concatenation (avoid - error-prone)
# full_url = f"{api_url}/users?username=qa_user&status=active"  # ❌ Risky

    URL Query String Syntax Breakdown
            Symbol	Purpose	Rules
                ?	Starts the query string	Only ONE ? per URL, must come after the path
                &	Separates key-value pairs	Use between each parameter
                =	Assigns value to key	One per parameter


# Method 4: Parse existing URLs
parsed = urlparse(full_url)
query_params = parse_qs(parsed.query)  # Returns dict of params
"""

print("------------------ os ------------------------")  
from dotenv import load_dotenv
import os

load_dotenv()  # Loads from .env file

# 1) Read environment variables
api_url = os.getenv("API_URL", "http://localhost:8000")
# If missing, returns default

# Required variable pattern
token = os.getenv("API_TOKEN")
if not token:
    raise RuntimeError("Missing API_TOKEN")

# 2) Current working directory
cwd = os.getcwd()
print("Current folder:", cwd)

# 3) Join paths safely (portable between Linux/Windows)
report_path = os.path.join(cwd, "reports", "result.json")
print("Report path:", report_path)

# 4) Check path/file existence
if os.path.exists(report_path):
    print("Report exists")

# 5) Create directories (if needed)
os.makedirs(os.path.join(cwd, "reports"), exist_ok=True)

# 6) List files in a directory
for name in os.listdir(cwd):
    print(name)

# 7) Run a shell command (simple, but prefer subprocess in serious code)
exit_code = os.system("echo Hello from shell")
print("Exit code:", exit_code)


print("------------------ re (regex) ------------------------")
import re

# Text samples
text = "error info debug error 1234 john123"
email = "qa_user@example.com"
log_line = "ERROR: Connection timeout at 2025-01-28 14:30:45"

# 1) findall() - returns LIST of ALL matches (anywhere in string)
print("\n=== findall() ===")
words = re.findall(r"\w+", text)  # All word characters
print(f"Words: {words}")  # ['error', 'info', 'debug', 'error', '1234', 'john123']

numbers = re.findall(r"\d+", text)  # All digit sequences
print(f"Numbers: {numbers}")  # ['1234', '123']

# 2) match() - checks START of string only, returns Match object or None
print("\n=== match() ===")
if re.match(r"\w+", text):  # Starts with word? YES
    print(f"✓ Text starts with word")

if re.match(r"\d", text):  # Starts with digit? NO
    print(f"✓ Text starts with digit")
else:
    print(f"✗ Text does NOT start with digit")

# 3) search() - finds FIRST match ANYWHERE, returns Match object or None
print("\n=== search() ===")
match = re.search(r"\d+", text)  # Find first number
if match:
    print(f"First number found: {match.group()}")  # '1234'
    print(f"Position: {match.start()}-{match.end()}")  # 33-37

# 4) sub() - replace matches
print("\n=== sub() ===")
censored = re.sub(r"\d", "X", text)
print(f"Censored: {censored}")  # error info debug error XXXX johnXXX

# 5) Common patterns for QA testing
print("\n=== Common QA patterns ===")
email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
is_valid_email = bool(re.match(email_pattern, email))
print(f"Valid email: {is_valid_email}")

has_error = bool(re.search(r'ERROR', log_line))
print(f"Has ERROR in logs: {has_error}")

timestamp_match = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', log_line)
if timestamp_match:
    print(f"Extract timestamp: {timestamp_match.group()}")
    
"""
================================================================

pattern1 = r'[a-zA-Z0-9_.+-]+'  # ONE OR MORE of these chars
test_strings = [
    "john_doe",        # ✓ letters + underscore
    "qa+tag",          # ✓ letters + plus
    "user.name",       # ✓ letters + dot
    "test-123",        # ✓ letters + hyphen + digits
    "valid_email.part" # ✓ mixed
]

================================================================

# Pattern 1: Just one character
pattern1 = r'[a-z]'
print(re.findall(pattern1, "hello"))  # ['h', 'e', 'l', 'l', 'o']

# Pattern 2: One or MORE characters (a whole word)
pattern2 = r'[a-z]+'
print(re.findall(pattern2, "hello world 123"))  # ['hello', 'world']

# Pattern 3: Inside brackets, + is LITERAL (not a quantifier)
pattern3 = r'[a-z+]'
print(re.findall(pattern3, "a+b"))  # ['a', '+', 'b']

# Pattern 4: Both literal + AND quantifier
pattern4 = r'[a-z+]+'
print(re.findall(pattern4, "a+b++c"))  # ['a+b++c'] - matches "word with plus signs"

================================================================

text = "hello world 123"
pattern = r"\d+"

# match() checks ONLY the START
match_result = re.match(pattern, text)
print(match_result)  # None (because text starts with "hello", not a digit)

# search() looks ANYWHERE
search_result = re.search(pattern, text)
print(search_result)  # <re.Match object> (finds "123" at the end)
print(search_result.group())  # "123"

================================================================
"""

print("------------------ logging ------------------------")
import logging

# 1) Set up ONCE (in a fixture or at module start)
logging.basicConfig(
    level=logging.INFO,  # Use constant, not string
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('./T24_T3/test_results.log'),  # File output
        logging.StreamHandler()  # Console output
    ]
)

# 2) Create logger instance (reusable)
logger = logging.getLogger(__name__)
print(f"__name__ : {__name__}")
# 3) Use it
logger.info("Hi Hello")
logger.debug("Detailed info for debugging") # hidden because of the level=logging.INFO
logger.warning("Something might be wrong")
logger.error("Operation failed")

print("------------------ collections ------------------------")
from collections import defaultdict, Counter

# defaultdict: Automatically creates default value for missing keys
print("\n=== defaultdict ===")
# Without defaultdict, accessing missing key raises KeyError
# With defaultdict(list), missing key gets empty list []
test_results = defaultdict(list)
# defaultdict(list) creates a dictionary where any missing key 
# automatically gets an empty list [] as its default value.
print("-------------------ℹ️-----------------------")
print(test_results)
print("------------------------------------------")

test_results["login"].append("PASS")
test_results["login"].append("FAIL")
test_results["logout"].append("PASS")
print(f"Test results: {dict(test_results)}")
# Output: {'login': ['PASS', 'FAIL'], 'logout': ['PASS']}

# Without defaultdict (verbose & error-prone):
"""
test_results_manual = {}
if "login" not in test_results_manual:
    test_results_manual["login"] = []
test_results_manual["login"].append("PASS")
test_results_manual["login"].append("FAIL")

if "logout" not in test_results_manual:
    test_results_manual["logout"] = []
test_results_manual["logout"].append("PASS")
print(f"Test results (manual): {test_results_manual}")

# OR using .setdefault() (less verbose):
test_results_alt = {}
test_results_alt.setdefault("login", []).append("PASS")
test_results_alt.setdefault("login", []).append("FAIL")
test_results_alt.setdefault("logout", []).append("PASS")
print(f"Test results (setdefault): {test_results_alt}")
"""


# Another example: count failures per test
failure_counts = defaultdict(int)
failure_counts["test_api"] += 1
failure_counts["test_ui"] += 2
failure_counts["test_api"] += 1
print(f"Failures: {dict(failure_counts)}")
# Output: {'test_api': 2, 'test_ui': 2}


# #################################################################
# Counter: Count occurrences of items
print("\n=== Counter ===")
# Common in QA: count test statuses
test_statuses = ["PASS", "PASS", "FAIL", "PASS", "SKIP", "FAIL"]
status_count = Counter(test_statuses)
print(f"Status counts: {status_count}")
# Output: Counter({'PASS': 3, 'FAIL': 2, 'SKIP': 1})

# Most common 2 results
print(f"Top 2 statuses: {status_count.most_common(2)}")
# Output: [('PASS', 3), ('FAIL', 2)]

# Count words in log line (useful for log analysis)
log_text = "error warning error info error warning error"
words = log_text.split()
print(f"Words {words}")
word_count = Counter(words)
print(f"Word count: {word_count}")
# Output: Counter({'error': 4, 'warning': 2, 'info': 1})
print(f"Word dict: {dict(word_count)}")

print("-----------------------------")
print({"a":[]})

print("------------------ json schema ------------------------")
from jsonschema import validate, ValidationError

# Define what a valid "person" object must look like
schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age":  {"type": "integer", "minimum": 0},
        "email": {"type": "string", "format": "email"},
    },
    "required": ["name", "age"],  # these keys must always be present
}

person = {"name": "Alice", "age": 30, "email": "alice@example.com"}

try:
    validate(instance=person, schema=schema)
    print("Valid JSON!")
except ValidationError as e:
    print(f"Invalid JSON: {e.message}")

# Invalid example – age is a string instead of integer
bad_person = {"name": "Bob", "age": "thirty"}
try:
    validate(instance=bad_person, schema=schema)
    print("Valid JSON!")
except ValidationError as e:
    print(f"Invalid JSON: {e.message}")
    


