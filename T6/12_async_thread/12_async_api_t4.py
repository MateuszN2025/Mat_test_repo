import requests
import asyncio
import subprocess
import time
from functools import wraps
from async_thread_func import display


subprocess.run(args="clear")
print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n")

POKE_URL = "https://pokeapi.co/api/v2/"

def log_time(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        t1 = time.perf_counter_ns()
        # print(f"||| {func.__name__} |||")
        result = await func(*args, **kwargs)
        t2 = time.perf_counter_ns()
        td = t2 - t1
        print(f"{display('ASYNC')}")
        print(f"🟪 td = {int(td // 1e6)} ms |args={args} kwargs={kwargs}| ||| {func.__name__} |||")
        # print(f"td = {td:.0f} |{args}|")
        return result

    return wrapper
        
# @log_time
async def api_call(number):
    # print(f"▶️ API call number : {number} start.")
    try:
        response = await asyncio.to_thread(requests.get, POKE_URL, timeout=10)
        response.raise_for_status()
    except requests.RequestException as exc:
        print(f"❌ API call number : {number} failed. error={exc}")
        return None

    # print(f"✅ API call number : {number} end. status={response.status_code}")
    return response.status_code

@log_time
async def process_api_calls():

    # results = [x1, x2, ...]
    # *results = x1 , x2 ...
    
    # results = await asyncio.gather(*[(api_call(i)) for i in range(10)])
    results = await asyncio.gather(*(api_call(i) for i in range(10)))
    # [...] -> list comprehension, creates the whole list immediately
    # (...) in this context -> generator expression, not a tuple
    
    # api_call(i) does not run the function body immediately.
    # It creates a coroutine object. The actual work starts 
    # when gather awaits and schedules those coroutines.
    # coroutines = [api_call(i) for i in range(10)]
    # await asyncio.gather(*coroutines)
    
    """
    GENERATOR EXPRESSION
    
    (api_call(i) for i in range(10))
    
    def gen():
        for i in range(10):
            yield api_call(i)
            
    (x for x in items)
    
    def temp():
        for x in items:
            yield x
        """
    
    # results = await asyncio.gather(
    #     api_call(1),
    #     api_call(2),
    #     api_call(3),
    #     api_call(4)        
    # )
    # print(f"Results: {results}")
    # return results
    

asyncio.run(process_api_calls())

print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")  # noqa: E303

"""
async def api_call(number):
    ...
does not run immediately when you write:
    api_call(3) 
It creates a coroutine object.

gen = (api_call(i) for i in range(3))

ℹ️ Iterable:
items = [1, 2, 3]
for x in items:
    print(x)

ℹ️ Iterator:
it = iter([1, 2, 3])
print(next(it))

ℹ️ Generator:
def squares():
    for i in range(3):
        yield i * i

ℹ️ Coroutine:
async def work():
    await asyncio.sleep(1)
    return "done"
"""
