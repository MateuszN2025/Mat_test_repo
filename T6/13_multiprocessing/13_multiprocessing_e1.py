import asyncio
import threading
import multiprocessing
import time
import subprocess
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import requests
import aiohttp
from functools import wraps


URL = "https://pokeapi.co/api/v2/"
RANGE = 10

def log_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t1 = time.perf_counter_ns()
        result = func(*args, **kwargs)
        t2 = time.perf_counter_ns()
        td = t2 - t1
        print(f"td = {int(td/1e6)} ms |{func.__name__}|")
        return result
    return wrapper

def call_api(_: int | None = None):
    response = requests.request("GET", URL)
    return response.status_code

def call_apis_processing_threads():
    # threads = [threading.Thread(target=call_api) for _ in range(RANGE)]
    # for thread in threads:
    #     thread.start()
    # for thread in threads:
    #     thread.join()
    # return threads
    with ThreadPoolExecutor(max_workers=RANGE) as executor:
      return list(executor.map(call_api, range(RANGE)))
		

@log_time
def main1_threads():
    return call_apis_processing_threads()

def call_apis_processing_multi():
    # processes = [multiprocessing.Process(target=call_api) for _ in range(RANGE)]
    # for process in processes:
    #     process.start()
    # for process in processes:
    #     process.join()
    # return processes
    with ProcessPoolExecutor(max_workers=RANGE) as executor:
      return list(executor.map(call_api, range(RANGE)))


@log_time
def main2_multi():
    return call_apis_processing_multi()

def log_time_async_aiohttp(func):
    @wraps(func)
    async def wrapper_async(*args, **kwargs):
        t1 = time.perf_counter_ns()
        result = await func(*args, **kwargs)
        t2 = time.perf_counter_ns()
        td = t2 - t1
        print(f"td = {int(td/1e6)} ms |{func.__name__}|")
        return result
    return wrapper_async

async def call_api_asyncio():
    return await asyncio.to_thread(call_api)

async def call_apis_processing_asyncio():
    return await asyncio.gather(*(call_api_asyncio() for _ in range(RANGE)))

@log_time_async_aiohttp
async def main3_asyncio():
    return await call_apis_processing_asyncio()
    
    
async def call_api_aiohttp(session: aiohttp.ClientSession):
    async with session.get(URL) as response:
        return response.status

async def call_apis_processing_aiohttp():
    async with aiohttp.ClientSession() as session:
        return await asyncio.gather(*(call_api_aiohttp(session) for _ in range(RANGE)))

@log_time_async_aiohttp
async def main4_aiohttp():
    return await call_apis_processing_aiohttp()
    

def run_all():
    subprocess.run(args="clear")
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n")
    main1_threads()
    main2_multi()
    asyncio.run(main3_asyncio())
    asyncio.run(main4_aiohttp())
    print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")


if __name__ == "__main__":
    run_all()
