"""
Basic tutorial: asyncio vs threading vs multiprocessing.

Run this file directly to see three small examples:
1. asyncio: many I/O-like waits in one thread
2. threading: overlapping blocking I/O work
3. multiprocessing: splitting CPU work across processes

Rule of thumb:
- asyncio -> best for many network/file/database waits
- threading -> good for blocking I/O libraries
- multiprocessing -> good for CPU-heavy calculations
"""

from __future__ import annotations

import asyncio
import multiprocessing as mp
import threading
import time

import subprocess


def section(title: str) -> None:
    print(f"\n{'=' * 20} {title} {'=' * 20}")


async def async_download(name: str, delay: float) -> str:
    print(f"{name}: start async wait for {delay}s")
    await asyncio.sleep(delay)
    print(f"{name}: async work finished")
    return f"{name} result"


async def async_example() -> None:
    section("ASYNCIO")
    print("One thread, many tasks, great for waiting on I/O.")
    start_time = time.perf_counter()

    results = await asyncio.gather(
        async_download("task-1", 1.5),
        async_download("task-2", 1.0),
        async_download("task-3", 0.5),
    )

    elapsed = time.perf_counter() - start_time
    print(f"Results: {results}")
    print(f"Async total time: {elapsed:.2f}s")


def blocking_io_task(name: str, delay: float) -> None:
    print(f"{name}: start blocking work for {delay}s")
    time.sleep(delay)
    print(f"{name}: blocking work finished")


def threading_example() -> None:
    section("THREADING")
    print("Multiple threads can overlap blocking I/O calls.")
    start_time = time.perf_counter()

    threads = [
        threading.Thread(target=blocking_io_task, args=("thread-1", 1.5)),
        threading.Thread(target=blocking_io_task, args=("thread-2", 1.0)),
        threading.Thread(target=blocking_io_task, args=("thread-3", 0.5)),
        # multiprocessing.Process(target=worker, args=(i,))
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    elapsed = time.perf_counter() - start_time
    print(f"Threads total time: {elapsed:.2f}s")


def cpu_heavy_task(limit: int) -> int:
    total = 0
    for number in range(limit):
        total += number * number
    return total


def multiprocessing_example() -> None:
    section("MULTIPROCESSING")
    print("Separate processes help with CPU-heavy work.")
    start_time = time.perf_counter()

    limits = [2_000_000, 2_000_000, 2_000_000]
    with mp.Pool(processes=3) as pool:
        # Creates a pool of 3 worker processes.
        # A process is separate from the main Python process, 
        # so it can use another CPU core.
        results = pool.map(cpu_heavy_task, limits)
        # It does this internally:
        # cpu_heavy_task(2_000_000)
        # cpu_heavy_task(2_000_000)
        # cpu_heavy_task(2_000_000)
        # but done in parallel processes instead of one after another.

    elapsed = time.perf_counter() - start_time
    print(f"Process results sample: {results[0]}")
    print(f"Multiprocessing total time: {elapsed:.2f}s")


def main() -> None:

    subprocess.run(args="clear")
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n")

    print("Python concurrency tutorial")
    print("Use asyncio for async I/O, threads for blocking I/O, processes for CPU work.")
    asyncio.run(async_example())
    threading_example()
    multiprocessing_example()

    print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")  # noqa: E303


if __name__ == "__main__":
    # multiprocessing needs the if __name__ == "__main__": guard, especially on Windows.
	main()

