import aiohttp
import asyncio
import sys
from pathlib import Path
import helpers as h
import requests
# print(f">>> {Path(__file__).resolve().parents[3] / 'T6' / '12_async_thread' / 'helpers'}")

URL = "https://pokeapi.co/api/v2/"

# === asyncio aiohttp ===
async def api_call(session):
    async with session.get(URL) as response:
        return await response.text()

# === asyncio ===
# async def api_call():
#     return await asyncio.to_thread(requests.get, URL)

# === asyncio aiohttp ===
async def api_calls_processing():
    # aiohttp.ClientSession -> async context managers
    async with aiohttp.ClientSession() as session:
        return await asyncio.gather(*(api_call(session) for i in range(10)))

# === asyncio ===
# async def api_calls_processing():
#     return await asyncio.gather(*(api_call() for i in range(10)))
    

@h.log_a
async def main():    
    await api_calls_processing()

if __name__ == "__main__":
    asyncio.run(main())