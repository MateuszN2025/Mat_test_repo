import threading
import time
import random

def log_time_thread(func):
    def wrapper(*args, **kwargs):
        t1 = time.perf_counter_ns()
        result = func(*args, **kwargs)
        t2 = time.perf_counter_ns()
        td = t2 - t1
        print(f"ℹ️ time: {td//1e6:.2f}")
        return result
    return wrapper


def task(id_num: int) -> None:
    print(f" ❗ id_num: {id_num}")
    time.sleep(random.randint(0, 4))

@log_time_thread
def run_tasks():
    t = threading.Thread(target=task, args=(1,))  # pass function, not call it
    t.start()
    t.join()
    
run_tasks()
    
    