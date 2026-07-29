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

print("----------------- ℹ️  async ℹ️ -------------------------")
import asyncio
import random

async def task(task_id: int) -> None:
    # Simulate variable I/O latency for each async task.
    await asyncio.sleep(random.randint(1, 3))
    print(f"Task id: {task_id}")

async def run_tasks() -> None:
    # Run both coroutines concurrently and wait until both complete.
    await asyncio.gather(task(1), task(2))
    
async def main1() -> None:
    await run_tasks()

if __name__ == "__main__":
    asyncio.run(main1())
    
    
print("----------------- ℹ️  threading ℹ️ -------------------------")
import threading
import time

def duty(duty_id: int) -> None:
    time.sleep(random.randint(1,3))
    print(f"Duty number: {duty_id}")
    
def execute_duties_in_threads() -> None:
    t1 = threading.Thread(target=duty, args=(1,)) 
    t2 = threading.Thread(target=duty, args=(2,))    
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
def main2() -> None:
    execute_duties_in_threads()
    

if __name__ == "__main__":
    main2()
    
print("----------------- ℹ️  multiprocessing ℹ️ -------------------------")

import multiprocessing

def execute_duties_in_processes() -> None:
    p1 = multiprocessing.Process(target=duty, args=(1,))
    p2 = multiprocessing.Process(target=duty, args=(2,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
def main3():
    execute_duties_in_processes()
    
# THIS IS REQUIRED for multiprocessing in Python
# because: creating a new process imports the main script from the top down.
# the new child process will read the file, hit that function call, 
# and spawn another child process. That child will spawn another, 
# and so on, leading to an infinite recursive loop and a crash
if __name__ == "__main__":
    main3()