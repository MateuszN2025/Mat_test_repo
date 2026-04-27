import asyncio
import requests
import time

URL1="https://pokeapi.co/api/v2/"

def logs(func):
    async def wrapper(*args, **kwargs):
        t1 = time.perf_counter_ns()
        result = await func(*args, **kwargs)
        t2 = time.perf_counter_ns()
        td = t2 - t1
        print(f"td: {int(td//1e6)} ms")
        return result
    return wrapper

async def api_call(num: int):
    # print(f"asyncio {num}")
    await asyncio.to_thread(requests.get, URL1)
    # await asyncio.sleep(0.5)

@logs
async def api_calls_processing():
    await asyncio.gather(*(api_call(i) for i in range(10)))    

# async def main():
#    await api_calls_processing()

# if __name__ == "__main__":
#     asyncio.run(main())

asyncio.run(api_calls_processing())