import functools
import threading
import time
import random

def log_time_thread(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        t1 = time.perf_counter_ns()
        result = func(*args, **kwargs)
        t2 = time.perf_counter_ns()
        td = t2 - t1
        # Convert ns -> ms with true division to preserve sub-millisecond precision
        print(f"ℹ️ time: {td / 1e6:.2f}")
        return result
    return wrapper


def task_sleep(id_num: int) -> None:
    print(f" ❗ id_num: {id_num}")
    time.sleep(random.randint(1, 4))

@log_time_thread
def run_tasks():
    
    t_list = []
    for t_id in range(10):
        t_list.append(threading.Thread(target=task_sleep, args=(t_id, )))  # pass function, not call it
        
    for th in t_list:   
        th.start()
        
    for th in t_list:   
        th.join()
    
run_tasks()
    
    