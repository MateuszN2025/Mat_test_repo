import asyncio
import subprocess
import time
from functools import wraps
from async_thread_func import display

import aiohttp


subprocess.run(args="clear")
print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n")

POKE_URL = "https://pokeapi.co/api/v2/"


def log_time(func):
	# wraps() keeps the original function metadata after decoration.
	@wraps(func)
	async def wrapper(*args, **kwargs):
		start_time = time.perf_counter_ns()
		result = await func(*args, **kwargs)
		elapsed_ms = (time.perf_counter_ns() - start_time) // 1_000_000
		print(f"{display('aiohttp')}")
		print(f"🟪 td = {elapsed_ms} ms | {func.__name__} | args={args} kwargs={kwargs}")
		return ""
	return wrapper


async def api_call(session: aiohttp.ClientSession, number: int) -> str | None:
	# Reuse one shared client session instead of opening a new connection per request.

	try:
		# async with waits for the HTTP response and closes the response object cleanly.
		async with session.get(POKE_URL) as response:
			response.raise_for_status()
			# JSON body reading is also asynchronous and must be awaited.
			data = await response.json()
	except aiohttp.ClientError as exc:
		print(f"❌ API call number: {number} FAILED | error={exc}")
		return None
	except asyncio.TimeoutError:
		print(f"❌ API call number: {number} FAILED | timeout")
		return None

	# print(f"✅ API call number: {number} END | status={response.status}")



@log_time
async def main() -> list[str | None]:
	# Put one timeout policy on the whole session.
	timeout = aiohttp.ClientTimeout(total=10)

	async with aiohttp.ClientSession(timeout=timeout) as session:
		# gather schedules all coroutine objects and waits until all of them finish.
		return await asyncio.gather(*(api_call(session, number) for number in range(10)))


if __name__ == "__main__":
	results = asyncio.run(main())
	# print(f"results={results}")
	print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")  # noqa: E303