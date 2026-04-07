# import threading
# import time
#
# '''
# What happens:
# Both threads start almost simultaneously.
# time.sleep doesn’t block other threads.
# Good for I/O tasks.
# '''
#
# def task(name):
#     print(f"{name} started")
#     time.sleep(2)  # simulate I/O
#     print(f"{name} finished")
#
# # Create threads
# t1 = threading.Thread(target=task, args=("Thread 1",))
# t2 = threading.Thread(target=task, args=("Thread 2",))
#
# # Start threads
# t1.start()
# t2.start()
#
# # Wait for threads to finish
# t1.join()
# t2.join()
#
# print("All threads done!")






# import threading
# import time
#
# def task(name:str):
#     print(f"start the connection of process {name}\n")
#     time.sleep(1)
#     print(f"end the connection of process {name}\n")
#
# t1 = threading.Thread(target=task, args=("thread 111",))
# t2 = threading.Thread(target=task, args=("thread 222",))
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()






import threading
import time

def task(name:str):
    print(f"Connection to {name} started.\n")
    time.sleep(2)
    print(f"Connection to {name} ended.\n")


tt11 = threading.Thread(target=task, args=("thread 222",))
tt22 = threading.Thread(target=task, args=("thread 333",))

tt11.start()
tt22.start()

tt11.join()
tt22.join()










































