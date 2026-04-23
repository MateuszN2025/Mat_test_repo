import asyncio
import random
import subprocess
subprocess.run(args="clear")
print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n")



async def io_reading(name: str="io_port", delay: int=1):
    """
    async fun
    """
    print(f"Staring '{name}' reading")
    await asyncio.sleep(delay)
    print(f"Finished '{name}' after {delay}s delay")

async def io_processing():
    io_tasks = {
        "io_1": random.randint(1, 4),
        "io_2": random.randint(1, 4),
        "io_3": random.randint(1, 4),
    }
    # await asyncio.gather(io_reading(), io_reading() )
    
    # tasks = [io_reading(io_name, io_delay) for io_name, io_delay in io_tasks.items()]
    # await asyncio.gather(*tasks)
    
    """
    *tasks
    tasks = [task1, task2, task3] -> 
        asyncio.gather(*tasks) ->
            asyncio.gather(task1, task2, task3)

    """
    
    
    # await asyncio.gather(
    #     *(io_reading(io_name, io_delay) for io_name, io_delay in io_tasks.items())
    #     )
    
    await asyncio.gather(
        io_reading("io_1", 1),
        io_reading("io_2", 2),
        io_reading("io_3", 3),
        )
    
asyncio.run(io_processing())
    
# #######################################################
async def process():       # async def defines coroutines
    await asyncio.sleep(1) # await pauses without blocking the event loop
    pass

async def run_processes(): # async def defines coroutines
    await asyncio.gather(  # await pauses without blocking the event loop
                         # asyncio.gather(...) -> runs multiple coroutines concurrently
        process(),
        process(),
        process())
    pass

asyncio.run(run_processes()) # starts the event loop
# #######################################################
"""
waiting on network/files/API/database: use asyncio
blocking library calls: often threading
heavy CPU work: use multiprocessing
"""

    



print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")  # noqa: E303
