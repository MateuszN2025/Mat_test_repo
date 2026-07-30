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