import asyncio
import requests
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

POKE_URL = "https://pokeapi.co/api/v2/"

async def api_call():
    await asyncio.to_thread(requests.get, POKE_URL)
    
async def process_api_calls():
    await asyncio.gather(*(api_call() for _ in range(20)))  # gather takes *args, not a list

@log_time
async def main():
    await process_api_calls()  # already inside async context, just await


if __name__ == "__main__":
    asyncio.run(main())  # asyncio.run() belongs 
    # at the entry point, not inside async def
    # asyncio in one sentence: Run many tasks that spend most
    # of their time waiting (network, disk) without spawning
    # threads — one thread, one event loop, tasks take turns.
    
    """
    Thread
    │
    └── Event Loop
        ├── task1: fetch()   → awaits I/O → paused
        ├── task2: fetch()   → awaits I/O → paused
        ├── task3: fetch()   → awaits I/O → paused
        │
        │   (OS notifies: task2's I/O is done)
        │
        └── task2: resumes → finishes
    """
    