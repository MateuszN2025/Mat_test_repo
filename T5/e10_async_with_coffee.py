import asyncio


async def make_coffee():
    print("Coffee started")
    await asyncio.sleep(3)  # simulates coffee making
    print("Coffee ready!")
    return "☕"


async def eat_croissant():
    print("Croissant started")
    await asyncio.sleep(1)  # simulates eating time
    print("Croissant done!")
    return "🥐"


async def breakfast():
    print("Breakfast started")

    coffee = await make_coffee()  # ← await pauses breakfast coroutine until coffee is ready
    croissant = await eat_croissant()  # ← await pauses until croissant done

    print(f"Breakfast done: {coffee} + {croissant}")


asyncio.run(breakfast())

'''
Step by step execution:
breakfast() starts.
await make_coffee() → pauses breakfast() coroutine until make_coffee() finishes.
make_coffee() sleeps 3 seconds (asyncio.sleep(3) is awaitable).
While sleeping, other coroutines could run if there were any.
After 3 seconds, make_coffee() completes → breakfast() resumes.
await eat_croissant() → pauses again for 1 second.
When done → breakfast() prints result.

4️⃣ Key Observations
The awaited “task” is what comes after await.
Example: await make_coffee() → the task is make_coffee().
await pauses only the current coroutine, not the whole program.
Async allows concurrent operations without using threads.
'''