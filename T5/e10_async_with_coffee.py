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