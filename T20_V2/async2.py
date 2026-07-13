import asyncio
import time

def log_time(func):
    async def wrapper(*args, **kwargs):
        t1 = time.perf_counter_ns()
        print(f"ℹ️  start time:{(t1):.2f}")
        result = await func(*args, **kwargs)
        t2 = time.perf_counter_ns()
        print(f"✅  end time:{(t2):.2f}")
        td = t2 - t1
        print(f"⚠️  time diff: {td/1e6:.2f}")
        return result
    return wrapper

async def task_exe(id_name) -> None:
    print(f"id: {id_name}")
    await asyncio.sleep(1)  # asyncio.sleep yields control; time.sleep blocks the event loop

@log_time
async def run_tasks() -> None:
    # tasks = []
    # for t in range(10):
    #     tasks.append(task_exe(t))  # collect coroutines first
    # await asyncio.gather(*tasks)  # run all 10 tasks concurrently
    # await asyncio.gather(*((task_exe(t) for t in range(10)))) 
    await asyncio.gather(task_exe(1), task_exe(2))
    
asyncio.run(run_tasks())