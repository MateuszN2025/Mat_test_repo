import asyncio

'''
What happens:
Single thread handles multiple tasks using the event loop.
await allows switching between tasks while waiting.
Perfect for high-concurrency I/O.
'''

async def task(name):
    print(f"{name} started")
    await asyncio.sleep(2)  # simulate I/O
    print(f"{name} finished")

async def main():
    # Run both tasks concurrently
    await asyncio.gather(
        task("Async Task 1"),
        task("Async Task 2")
    )

asyncio.run(main())
print("All async tasks done!")