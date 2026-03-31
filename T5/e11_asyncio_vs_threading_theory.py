# Main differences:
#
# Programming model
# threading works with regular def functions
# asyncio requires async def, await, and async-compatible libraries
# Scheduling
# threading is scheduled by the OS
# asyncio is scheduled by the event loop when coroutines await
# Cost
# threads are heavier than coroutines
# asyncio can handle many concurrent tasks efficiently if they spend time waiting
# Shared state
# threads share memory concurrently, so race conditions and locks are common concerns
# asyncio usually runs tasks in one thread, so many thread-safety issues are reduced, though shared mutable state can still cause logical bugs
# Library compatibility
# threading can be used with blocking libraries
# asyncio works best only with non-blocking async libraries like aiohttp, async DB clients, async sockets
# CPU-bound work
# Neither is ideal for CPU-bound parallelism in standard CPython:
#
# threads are limited by the GIL for Python bytecode
# asyncio is not for CPU-heavy work at all
# For CPU-bound tasks, prefer:
#
# multiprocessing
# process pools
# native extensions that release the GIL
# When to use threading:
#
# you have blocking libraries
# you need simple background tasks
# you are integrating with older synchronous code
# concurrency level is moderate
# When to use asyncio:
#
# you have many concurrent network or I/O operations
# your libraries support async
# you want scalable I/O handling with low overhead
# you are building servers, crawlers, message consumers, websocket systems
# A useful rule:
#
# If your ecosystem is synchronous, use threads.
# If your ecosystem is async, stay async end to end.
# Do not mix them casually.
# One subtle but important point:
# asyncio is not “faster than threading” in general. It is often more scalable for lots of waiting tasks, but only if the whole stack is async-aware.
#
# Examples:
#
# Downloading 5 web pages: either works
# Handling 50,000 idle socket connections: asyncio is usually much better
# Running 4 heavy computations: neither asyncio nor threads is the right answer; use processes
# A compact analogy:
#
# threading: many workers, each can block independently
# asyncio: one worker juggling many tasks, but tasks must politely hand control back