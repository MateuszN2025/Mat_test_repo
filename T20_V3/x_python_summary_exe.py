print("----------------- ℹ️  classes ℹ️ -------------------------")
class Device:
    def __init__(self, size: str, category: str):
        self.size = size
        self.category = category
        
    def show_device_info(self):
        device_info = f"Size: {self.size}, category: {self.category}"
        print(device_info)
        return device_info
        
class Smartphone(Device):
    def __init__(self, company: str, model: str, size: str, category: str):
            self.company = company
            self.model = model
            super().__init__(size, category)
        
    def show_device_info(self):
        device_info = (
            f"Company: {self.company},"
            f"model: {self.model},"
            f"category: {self.category}"
        )
        # device_info = f"Company: {self.company}, \
        #                 model: {self.model}, \
        #                 size: {self.size}, \
        #                 category: {self.category}"
                            # When you use \ to break a line, 
                            # Python keeps all the whitespace (indentation)
                            # on the next line as literal spaces in the string
                                    # Company: Samsung,                         model: S24,                         size: small,                         c
                        
        print(device_info)
        return device_info

class Laptop(Device):
    def __init__(self, cpu: str, diagnoal: int, size: str, category: str):
            self.cpu = cpu
            self.diagnoal = diagnoal
            super().__init__(size, category)          
            
        
    def show_device_info(self):
        device_info = (
            f"Cpu: {self.cpu},"
            f"diagnoal: {self.diagnoal},"
            f"size: {self.size},"
            f"category: {self.category}"
        )
        print(device_info)
        return device_info

class Warehouse:
    def __init__(self):
        self.list1 = []
    
    def add_to_warehouse(self, element: str = None) -> list[str]:
        self.list1.append(element)
        return self.list1

d1 = Device("Big", "Home")
d1.show_device_info()

s1 = Smartphone("Samsung", "S24", "small", "private")
s1.show_device_info()

l1 = Laptop("intel", 15, "medium", "public")
l1.show_device_info()

print("--------------------")
w = Warehouse()

w.add_to_warehouse(s1)
w.add_to_warehouse(l1)

current_warehouse = w.add_to_warehouse()
print("--------------------")
print(current_warehouse)

print("----------------- ℹ️  POKEMON ℹ️ -------------------------")

url_pokemon = "https://pokeapi.co/api/v2/pokemon/ditto"

print("----------------- ℹ️  async ℹ️ -------------------------")
import asyncio
import random
import time
import requests

print("----------------- ℹ️  async wrapper ℹ️ ")
def time_logger(func):
    async def tl_wrapper(*args, **kwargs):
        t1 = time.perf_counter_ns()
        result = await func(*args, **kwargs)
        t2 = time.perf_counter_ns()
        td = (t2 - t1) // 1e6
        print(f"❗td: {td} ms ❗")
        return result
    return tl_wrapper
        

async def task(task_id: int) -> None:
    # Simulate variable I/O latency for each async task.
    # await asyncio.sleep(random.randint(1, 3))
    # await asyncio.sleep(2)
    await asyncio.to_thread(requests.get, url=url_pokemon)
    # Why this works:
    #   requests.get returns a normal Response object, 
    #   not a coroutine, so it cannot be awaited directly.
    #   asyncio.to_thread runs that blocking call in a 
    #   worker thread and returns something awaitable.
    print(f"Task id: {task_id}")

async def run_tasks() -> None:
    # Run both coroutines concurrently and wait until both complete.
    await asyncio.gather(task(1), task(2))
    
@time_logger  
async def main1() -> None:
    await run_tasks()
    
if __name__ == "__main__":
    # asyncio.run(main1())
    pass
    
    
print("----------------- ℹ️  threading ℹ️ -------------------------")
import threading
import time

def time_logger2(func):
    def tl_wrapper2(*args, **kwargs):
        t1 = time.perf_counter_ns()
        result = func(*args, **kwargs)
        t2 = time.perf_counter_ns()
        td = (t2 - t1) // 1e6
        print(f"❗td: {td} ms ❗")
        return result
    return tl_wrapper2


def duty(duty_id: int) -> None:
    # time.sleep(random.randint(1,3))
    requests.get(url=url_pokemon)
    print(f"Duty number: {duty_id}")
    
def execute_duties_in_threads() -> None:
    t1 = threading.Thread(target=duty, args=(1,)) 
    t2 = threading.Thread(target=duty, args=(2,))    
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()

@time_logger2
def main2() -> None:
    execute_duties_in_threads()
    

if __name__ == "__main__":
    # main2()
    pass
    
print("----------------- ℹ️  multiprocessing ℹ️ -------------------------")

import multiprocessing

def execute_duties_in_processes() -> None:
    p1 = multiprocessing.Process(target=duty, args=(1,))
    p2 = multiprocessing.Process(target=duty, args=(2,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()

@time_logger2
def main3():
    execute_duties_in_processes()
    
# THIS IS REQUIRED for multiprocessing in Python
# because: creating a new process imports the main script from the top down.
# the new child process will read the file, hit that function call, 
# and spawn another child process. That child will spawn another, 
# and so on, leading to an infinite recursive loop and a crash
if __name__ == "__main__":
    # main3()
    pass
    
    
print("----------------- ℹ️  getter and setters ℹ️ -------------------------")
class Secret:
    def __init__(self, name, password):
        self._name = name
        self.__password = password
        
    @property
    def getter(self):
        return self.__password
    
    @getter.setter # ❗
    def getter(self, new_password):
        self.__password = new_password
        
    @getter.deleter
    def getter(self):
        self.__password = 0
        # del self.__password     


s1 = Secret("user", "43278")
# print(repr(s1))

print(s1._name)
print(s1._Secret__password)
print("-----------------s1.getter-------------------------")
print(s1.getter)
print("-----------------s1.getter =------------------------")
s1.getter = "94309"
print("-----------------s1.getter-------------------------")
print(s1.getter)
print("-----------------s1.deleter-------------------------")
del s1.getter
print(s1.getter)
print("-----------------s1.getter =------------------------")
s1.getter = "11111"
print("-----------------s1.getter-------------------------")
print(s1.getter)

print("----------------- ℹ️  defaultdict ℹ️ -------------------------")
from collections import defaultdict, Counter

"""
d1 = {}
d1["t1"].append("PASSED")   # KeyError
"""
#     d1["t1"].append("PASSED")   # KeyError
#       KeyError: 't1'

d1 = {}
# Use normal dict when each key has a single value.
if "t1" not in d1:
    d1["t1"] = []
d1["t1"].append("PASSED")
print(f"d1|{d1}")

d2 = {}
d2.setdefault("t1", []).append("PASSED")
print(f"d2|{d2}")

dd_obj3 = defaultdict(list)
# Use defaultdict(list) when each key accumulates
# many values (append/grouping use cases).
dd_obj3["t1"].append("FAILED")
dd_obj3["t2"].append("FAILED")
dd_obj3["t3"].append("PASSED")
dd_obj3["t4"].append("SKIPPED")
dd_obj3["t5"].append("SKIPPED")
print(f"dd_obj3|{dd_obj3}")

d3 = dict(dd_obj3)
print(f"d3|{d3}")

print("------------------------------------------")
l4 = [v[0] for v in d3.values()]
# l4 = [v ❗ for v in d3.values()] # [['FAILED'], ['FAILED'], ['PASSED'], ['SKIPPED']]
print(l4)
c4 = Counter(l4)
print(c4)
print(c4.most_common(2))
d5 = dict(c4)
print(d5)

print("----------------- ℹ️  gc garbage collector ℹ️ -------------------------")

"""
For 99% of Python development, you never need to manually call gc.collect(), 
gc.disable(), or gc.enable(). Python handles memory management automatically in the background.
"""

import gc


class Node:
  pass


# Create a circular reference
a = Node()
b = Node()
a.peer = b
b.peer = a

# Remove external references
del a
del b

# Manually trigger the garbage collector
collected = gc.collect()
# gc.collect() when you need to force Python to clean up memory right now,
# rather than waiting for the automatic collector to trigger.
# gc.collect() immediately frees up RAM before your script 
# moves on to the next memory-heavy task.
# Wrapping the loading process in gc.disable() and gc.enable()
# can drastically speed up load times.
print(f"Unreachable objects collected: {collected}")

"""
Method,What it does,When you use it
gc.disable(),Turns OFF the automatic garbage collector.,
    "To prevent random performance pauses during time-critical tasks 
    (e.g., game loops, massive data imports)."
gc.enable(),Turns ON the automatic garbage collector 
    (this is the default state).,"To restore normal, automatic memory
    management after temporarily disabling it."
gc.collect(),Forces an immediate memory cleanup sweep.,"To instantly
    free up RAM after deleting huge datasets, or to manually 
    clean up memory during idle times while gc is disabled."
        Leave it enabled and forget about it for normal scripts. 
        Only use gc.collect() if you are dealing with massive amounts of data 
        and can't afford to wait for the automatic sweep.

import gc

# 1. Turn off automatic sweeps to prevent random pauses
gc.disable()

# 2. Run your performance-critical code (e.g., a game level, a real-time process)
# No unexpected GC pauses will happen here!
run_heavy_simulation()

# 3. Manually take out the trash when it is safe to do so (e.g., during a loading screen)
gc.collect()

"""

print("----------------- ℹ️  tricky  ℹ️ -------------------------")
a = 1
b = 1 
print(a is b)

print("----------------- ℹ️  Path  ℹ️ -------------------------")


from pathlib import Path

path_to_file = Path(__file__)
print(path_to_file)
file_dir = path_to_file.parent
print(file_dir)
file_dir_parents = path_to_file.parents[1]
print(file_dir_parents)

try:
    new_file = file_dir / "new_file.txt"
    # Create the file atomically; "x" mode raises FileExistsError if it already exists.
    with new_file.open("x", encoding="utf-8"):
        pass
except FileExistsError as e:
    print(e)
else:
    print("File created ✅")

print("----------------- ℹ️  shutil  ℹ️ -------------------------")

import shutil
new_file2 = file_dir / "new_file2.txt"
# shutil.copy(new_file, new_file2)
# new_file2.unlink()
new_file_dir = file_dir / "new_folder"
# new_file_dir.mkdir()

print("----------------- ℹ️  os  ℹ️ -------------------------")

import os
import dotenv

print(os.getenv("HOME"))
cwd = os.getcwd()
print(cwd)
print(dotenv.load_dotenv())
print("------------------------------------------")
print(os.getenv("MATVAR"))          # None if missing
print(os.environ.get("MATVAR"))     # same behavior
print(os.getenv("MATVAR", "not set"))  # with default fallback
print("------------------------------------------")
report_path = os.path.join(cwd, "reports", "result.json")
print("Report path:", report_path)
# 1) Create reports/ if missing
# os.makedirs(os.path.dirname(report_path), exist_ok=True)
# 2) Create/write the file
# data = {"status": "ok", "tests": 10}
# with open(report_path, "w", encoding="utf-8") as f:
# json.dump(data, f, indent=2)
# print("File created:", os.path.exists(report_path))
