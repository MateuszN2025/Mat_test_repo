import asyncio

# async def hello(): # funkcja asynchroniczna
#     print("Cześć")
#     # await - poczekaj, ale pozwól w tym czasie robić inne rzeczy
#     await asyncio.sleep(2)
#     # asynchroniczne czekanie
#     print("Minęły 2 sekundy")
#
# asyncio.run(hello()) # uruchamia program async
#
# '''
# import time
# # Program stoi i nic nie robi przez 2 sekundy.
# print("start")
# time.sleep(2)
# print("koniec")
# '''
#
# import asyncio
#
# async def task1():
#     print("task1 start")
#     await asyncio.sleep(2)
#     print("task1 koniec")
#
# async def task2():
#     print("task2 start")
#     await asyncio.sleep(1)
#     print("task2 koniec")
#
# async def main():
#     await asyncio.gather(task1(), task2())
#
# asyncio.run(main())


import time

async def task(n):
    print(f"start {n}")
    await asyncio.sleep(1)
    # time.sleep(1)
    print(f"koniec {n}")

'''
# 3sec
async def main():
    await task(1)
    await task(2)
    await task(3)
'''

# asyncio.gather() uruchamia wszystkie coroutines naraz w event loop.
async def main():
    await asyncio.gather(
        task(1),
        task(2),
        task(3)
    )

a = time.time()
asyncio.run(main())
b = time.time()
print(a-b)

'''
PROCESS
 ├── Thread
 ├── Thread
 └── Thread
(shared memory)

ASYNC (within a thread)
 Thread (single)
 └── Event Loop
      ├── Task
      ├── Task
      └── Task

MULTIPROCESS
 Process 1
 Process 2
 Process 3
(separate memory)
'''

'''
| Concept | Analogy                                         |
| ------- | ----------------------------------------------- |
| Thread  | Multiple cooks sharing one kitchen              |
| Async   | One cook switching between dishes while waiting |
| Process | Multiple separate kitchens                      |
'''

'''
Key Points

Threads
Multiple threads run inside one process.
Threads share memory, so communication is easy.
GIL allows only one Python bytecode instruction at a time, so CPU-bound threads don’t speed up much.
Great for I/O-bound tasks.

Async
Runs in a single thread.
Uses an event loop to switch between tasks while waiting.
new threads or processes are created.
Excellent for many concurrent I/O operations.

Processes
Each process is independent with its own memory.
True parallelism is possible (no GIL restriction).
Great for CPU-bound tasks.
'''

'''
| Feature     | Threading                      | Async                      |
| ----------- | ------------------------------ | -------------------------- |
| Concurrency | Multiple threads               | Single thread (event loop) |
| Ideal for   | I/O tasks, DB, files           | Many network requests      |
| CPU bound?  | Limited due to GIL             | Doesn’t help CPU-bound     |
| Syntax      | `threading.Thread(target=...)` | `async def` + `await`      |
'''