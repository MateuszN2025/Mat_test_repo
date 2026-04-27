import asyncio
import time
import aiohttp
import requests

POKE_URL = "https://pokeapi.co/api/v2/"

def logging(func):
    async def wrapper(*args, **kwargs):
        t1 = time.perf_counter_ns()
        result = await func(*args, **kwargs)
        t2 = time.perf_counter_ns()
        print(f"td: {(t2 - t1) // 1_000_000} ms")
        return result
    return wrapper

# async def api_call(session, num):
async def api_call(num):
    print(f"API call num: {num}")
    
    return await asyncio.to_thread(requests.get, POKE_URL)

    # async with session.get(POKE_URL) as response:
    #     return await response.text()

@logging
async def api_calls_processing():
    # async with aiohttp.ClientSession() as session:
    #     return await asyncio.gather(*(api_call(session, i) for i in range(10)))
    await asyncio.gather(*(api_call(i) for i in range(10)))

async def main():
    await api_calls_processing()

if __name__ == "__main__":
    asyncio.run(main())
    
