import multiprocessing
import time

def worker(num):
	print(f'Worker {num} starting')
	time.sleep(1)
	print(f'Worker {num} done')

if __name__ == "__main__":
	processes = []
	for i in range(4):
		p = multiprocessing.Process(target=worker, args=(i,))
		processes.append(p)
		p.start()
	for p in processes:
		p.join()
