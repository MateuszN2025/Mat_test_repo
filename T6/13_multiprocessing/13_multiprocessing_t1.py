
# Import the multiprocessing module to create and manage separate processes
import multiprocessing
# Import the time module to simulate work with sleep
import time


# Define a worker function that will be run in a separate process
# The function takes a single argument 'num' to identify the worker
def worker(num):
	# Print a message indicating the worker is starting
	print(f'Worker {num} starting')
	# Simulate some work by sleeping for 1 second
	time.sleep(1)
	# Print a message indicating the worker has finished
	print(f'Worker {num} done')


# The following block ensures this code only runs when the script is executed directly,
# not when imported as a module
if __name__ == "__main__":
	# Create a list to keep track of process objects
	processes = []
	# Launch 4 separate processes
	for i in range(4):
		# Create a new Process object, targeting the worker function with argument i
		# ############################################################################
  		# MULTIPROCESSING uses multiple processes, 
    	# each with its own Python interpreter and memory space.
     	# This allows true parallelism, especially for CPU-bound tasks,
      	# because each process runs independently and can utilize multiple CPU cores.
       	# Processes do not share memory, so communication is done via inter-process
        # communication (IPC) mechanisms like queues or pipes.
        # ############################################################################
        
		p = multiprocessing.Process(target=worker, args=(i,))
		# Add the process to the list
		processes.append(p)
		# Start the process (this runs worker(i) in a new process)
		p.start()
	# Wait for all processes to finish
	for p in processes:
		# join() blocks until the process completes
		p.join()

# ############################################################################
# THREADING uses multiple threads within a single process, sharing the same memory space.
# In Python, due to the Global Interpreter Lock (GIL), only one thread executes Python
# bytecode at a time, which limits true parallelism for CPU-bound tasks. 
# However, threading is useful for I/O-bound tasks (like file or network operations)
# because threads can run while others are waiting for I/O.
# ############################################################################


"""
With multiprocessing, you can run several independent processes, 
each with its own memory and Python interpreter.
Inside any of those processes, you can use threading to create 
multiple threads that share the same memory space (useful for I/O-bound tasks).
Also, within a single process, you can use asyncio to run many asynchronous
tasks on a single thread, switching between them when one is waiting (e.g., for I/O).
"""

"""
I/O-bound tasks are operations where the program spends most of its time waiting
for input/output (I/O) operations to complete, rather than using the CPU. Examples include:
Reading or writing files to disk
Network communication (sending/receiving data over the internet)
Waiting for user input
Database queries
In I/O-bound tasks, the CPU is often idle while waiting for data to be read or written,
so concurrency (using threads or async) can help improve efficiency
by allowing other tasks to run during these waiting periods.
"""