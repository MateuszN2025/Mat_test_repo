import multiprocessing
import time
import random
from functools import wraps

def log_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t1 = time.perf_counter_ns()
        result = func(*args, **kwargs)
        t2 = time.perf_counter_ns()
        td = t2 - t1
        print(f"time : {td / 1e6 :.2f}")
        return result
    return wrapper       


def call_task(id_num: int):
    print(f"id_num : {id_num}")
    time.sleep(random.randint(1,3))
    
@log_time
def run_call_tasks() -> None:
    multi_list = []
    for p_id in range(10):
        multi_list.append(multiprocessing.Process(target=call_task, args=(p_id,)))
        # Correct. Each multiprocessing.Process is a separate OS process with its own 
        # Python interpreter and its own GIL — so they don't share one.
    
    for pr in multi_list:
        pr.start()
    
    for pr in multi_list:
        pr.join()

    # Check for worker failures; exitcode != 0 means the process crashed or raised.
    failed = [pr for pr in multi_list if pr.exitcode != 0]
    if failed:
        raise RuntimeError(f"{len(failed)} worker(s) failed: {[pr.exitcode for pr in failed]}")

# Guard required for multiprocessing: without it, each spawned child re-imports
# this module and calls run_call_tasks() again, causing exponential process spawning
# on platforms that use the 'spawn' start method (Windows, macOS).
if __name__ == '__main__':
    run_call_tasks()
    