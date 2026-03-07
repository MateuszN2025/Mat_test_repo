import threading
import time

'''
What happens:
Both threads start almost simultaneously.
time.sleep doesn’t block other threads.
Good for I/O tasks.
'''

def task(name):
    print(f"{name} started")
    time.sleep(2)  # simulate I/O
    print(f"{name} finished")

# Create threads
t1 = threading.Thread(target=task, args=("Thread 1",))
t2 = threading.Thread(target=task, args=("Thread 2",))

# Start threads
t1.start()
t2.start()

# Wait for threads to finish
t1.join()
t2.join()

print("All threads done!")