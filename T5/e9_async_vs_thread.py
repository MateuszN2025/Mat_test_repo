import threading
import asyncio

# Async task
async def async_task(name):
    print(f"{name} started")
    await asyncio.sleep(2)  # simulate I/O
    # await pauses the coroutine until the awaited task completes.
    print(f"{name} finished")

# Function to run async tasks inside a thread
def thread_function(name):
    print(f"Thread {name} started")
    asyncio.run(async_task(f"Async inside {name}"))
    print(f"Thread {name} finished")

# Create threads
t1 = threading.Thread(target=thread_function, args=("Thread 1",))
t2 = threading.Thread(target=thread_function, args=("Thread 2",))

# Start threads
t1.start()
t2.start()

# Wait for threads to finish
t1.join()
t2.join()

print("All threads and async tasks done!")

'''
💡 This is the simplest real-world pattern for combining threads + async:
Use threads for parallelism (CPU or blocking tasks).
Use async inside a thread for high-concurrency I/O.
'''