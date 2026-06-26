import asyncio
import subprocess
subprocess.run(args="clear")
print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n")


async def io_process(name, delay):
    print(f"process: {name} started")
    await asyncio.sleep(delay)
    print(f"process: {name} finished")

async def io_process_execution():
    await asyncio.gather(
        io_process("io1", 1),
        io_process("io2", 2)
        )

asyncio.run(io_process_execution())


print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")  # noqa: E303

"""
asyncio is usually better when you have many I/O operations and your stack is async-aware.
Typical cases are many HTTP requests, WebSocket connections, async database drivers, async queues,
and high-concurrency servers. It scales well because one thread can manage many waiting tasks,
and context switching is cheap. The cost is that your code and libraries must cooperate with async and await.

threading is usually better when your work is I/O-bound but uses blocking libraries.
Typical cases are legacy code, blocking SDKs, blocking DB drivers, requests, 
file operations mixed with existing synchronous code, or small background tasks. 
It is often simpler to add to an existing synchronous program because you 
do not need to redesign everything around an event loop.

Use this rule:

If the library is async and you expect many concurrent waits, use asyncio.
If the library is blocking and you just need overlap for I/O, use threading.
If the work is CPU-heavy, use neither as the main solution; use multiprocessing.
Quick comparison:

asyncio: best for high numbers of concurrent waiting tasks
threading: best for integrating blocking I/O code with minimal redesign
asyncio: lower overhead, but requires async-compatible code
threading: easier to start with, but heavier and harder to reason about at scale
Examples:

Many API calls at once with aiohttp: use asyncio
Existing script using requests and you want 5 downloads in parallel: use threading
GUI app with one background worker: use threading
Chat server with thousands of connections: use asyncio
A simple mental shortcut:

“I can use await everywhere I need to wait” -> choose asyncio
“My code blocks and I don’t want to rewrite everything” -> choose threading
"""
