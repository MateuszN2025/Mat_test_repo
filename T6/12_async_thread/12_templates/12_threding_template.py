import threading
import time
import requests

URL = "https://pokeapi.co/api/v2/"

def log(func):
    def wrapper(*args, **kwargs):
        t1 = time.perf_counter_ns()
        func(*args, **kwargs)
        t2 = time.perf_counter_ns()
        td = t2 - t1
        print(f"td: {int(td//1e6)} ms")
    return wrapper

def api_call(id):
    # print(f"{id}")
    return requests.get(URL)

@log
def main():
    
    # 1 thread 
    # th1 = threading.Thread(target=api_call, args=(1,))
    # th1.start()
    # th1.join()
    
    threads = [threading.Thread(target=api_call, args=(i,)) for i in range(10)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    
    pass
    

if __name__ == "__main__":
    main()