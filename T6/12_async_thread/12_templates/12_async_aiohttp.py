import aiohttp
import asyncio
from helpers import log_a as h

URL = "https://pokeapi.co/api/v2/"

async def api_call(session: aiohttp.ClientSession):
    async with session.get(URL) as response:
        r = response.json()
        # print(f"type(r): {type(r)}") # type(r): <class 'coroutine'>
        return await r # <coroutine object ClientResponse.text at 0x79483ada3450>
@h
async def api_calls_processing():
    async with aiohttp.ClientSession() as session:
        rr = await asyncio.gather(*(api_call(session) for i in range(10)))
        # print(f"type(rr): {type(rr)}") # type(rr): <class 'list'>
        return rr
    
rrr = asyncio.run(api_calls_processing())
# print(f"{type(rrr)}")

    