import multiprocessing
import time
import requests
import threading
import asyncio
import aiohttp

import subprocess
subprocess.run(args="clear")
print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n")


URL = "https://pokeapi.co/api/v2/"
RANGE = 20

def logger(func):
    def wrapper(*args,**kwargs):
        t1 = time.perf_counter_ns()
        func(*args,**kwargs)
        t2 = time.perf_counter_ns()
        td = t2 - t1
        print(f"td: {int(td/1e6)} ms")
    return wrapper

def call_api():
    return requests.get(URL)

@logger
def main1():
    threads = [threading.Thread(target=call_api) for _ in range(RANGE)]

    for t in threads:
        t.start()
        
    for t in threads:    
        t.join()        
        
@logger
def main2():
    processes = [multiprocessing.Process(target=call_api) for _ in range(RANGE)]

    for p in processes:
        p.start()
        
    for p in processes:    
        p.join()
        
def logger_a(func):
    async def wrapper(*args,**kwargs):
        t1 = time.perf_counter_ns()
        await func(*args,**kwargs)
        t2 = time.perf_counter_ns()
        td = t2 - t1
        print(f"td: {int(td/1e6)} ms")
    return wrapper

async def call_api_async():
    return await asyncio.to_thread(requests.get, URL)
  
async def call_apis_processing_async():
    return await asyncio.gather(*(call_api_async() for _ in range(RANGE)))      

 
async def call_api_aiohttp(session: aiohttp.ClientSession):
    async with session.get(URL) as response:
        return await response.text()

async def call_apis_processing_aiohttp():
    async with aiohttp.ClientSession() as session:
        return await asyncio.gather(*(call_api_aiohttp(session) for i in range(RANGE)))

@logger_a
async def main3():
    await call_apis_processing_async() 
   
@logger_a
async def main4():
    return await call_apis_processing_aiohttp()


print("thread")
main1()
print("multi")
main2()
print("async")
asyncio.run(main3())
print("aiohttp")
asyncio.run(main4())

print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")  # noqa: E303

