"""
What happens:
Single thread handles multiple tasks using the event loop.
await allows switching between tasks while waiting.
Perfect for high-concurrency I/O.
"""

import asyncio
import random
import time

# async def task(name):
#     print(f"{name} started")
#     await asyncio.sleep(2)  # simulate I/O
#     print(f"{name} finished")
#
# async def main():
#     # Run both tasks concurrently
#     await asyncio.gather(
#         task("Async Task 1"),
#         task("Async Task 2")
#     )
#
# asyncio.run(main())
# print("All async tasks done!")

#
# print("===========================")
#
# async def io_conn(num):
#     print(f"Starting connection to IO number : {num}")
#     await asyncio.sleep(random.randint(1,10))
#     print(f"Connecting IO number : {num}...")
#     await asyncio.sleep(random.randint(1,10))
#     print(f"IO number : {num} connected!!!")
#
# async def conn_process():
#     await asyncio.gather(io_conn(1),io_conn(2))
#
# asyncio.run(conn_process())
#
# print("All async tasks done!")
#


print("<<<<<<<<<<<<>>>>>>>>>>>>>>")

async def io_fun(io_num):
    print(f"Connection to io num {io_num} started.")
    # t1 = random.randint(1,10)
    t1 = 3
    print(f" === Time of the connection: |{t1}sec| for io num {io_num} === ")
    await asyncio.sleep(t1) # let to switch to tasks while waiting

    '''
    <<<<<<<<<<<<>>>>>>>>>>>>>>
    Connection to io num 323 started.
     === Time of the connection: |3sec| for io num 323 === 
    Connection to io num 443 started.
     === Time of the connection: |3sec| for io num 443 === 
    Connection to io num 777 started.
     === Time of the connection: |3sec| for io num 777 === 
     Connection to io num 323 finished.
     Connection to io num 443 finished.
     Connection to io num 777 finished.
     
    Execution time: 3.0031001567840576
    '''

    # time.sleep(t1)
    '''
    <<<<<<<<<<<<>>>>>>>>>>>>>>
    Connection to io num 323 started.
     === Time of the connection: |3sec| for io num 323 === 
     Connection to io num 323 finished.
    Connection to io num 443 started.
     === Time of the connection: |3sec| for io num 443 === 
     Connection to io num 443 finished.
    Connection to io num 777 started.
     === Time of the connection: |3sec| for io num 777 === 
     Connection to io num 777 finished.
     
    Execution time: 9.002005100250244
    '''



    print(f" Connection to io num {io_num} finished.")

async def procced_with_io():
    await asyncio.gather(io_fun(323),io_fun(443),io_fun(777))


tx = time.time()
asyncio.run(procced_with_io())
ty = time.time()
print(f"Execution time: {ty-tx}")











