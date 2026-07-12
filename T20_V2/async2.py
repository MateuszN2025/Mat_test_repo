import asyncio


async def task1(id_name) -> None:
    print(f"id: {id_name}")
    await asyncio.sleep(1)  # asyncio.sleep yields control; time.sleep blocks the event loop

async def run_tasks() -> None:
    tasks = []
    for t in range(10):
        tasks.append(task1(t))  # collect coroutines first
    await asyncio.gather(*tasks)  # run all 10 tasks concurrently

asyncio.run(run_tasks())