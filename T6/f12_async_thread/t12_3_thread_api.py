import threading
import time
import requests
import subprocess
from functools import wraps
from async_thread_func import display
subprocess.run(args="clear")

POKE_URL = "https://pokeapi.co/api/v2/"

def log_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t1 = time.perf_counter_ns()
        func(*args, **kwargs)
        t2 = time.perf_counter_ns()
        td = t2 - t1
        print(f"{display('THREAD')}")
        print(f"🟪 td = {int(td // 1e6)} ms |args={args} kwargs={kwargs}| ||| {func.__name__} |||")
    return wrapper

# @log_time
def call_api(number):
    # print(f"▶️  API call number: {number} START")
    try:
        response = requests.get(url=POKE_URL)
    except requests.RequestException as exc:
        print(f"❌ API call number : {number} failed. error={exc}")
        return None
    # print(f"✅ API call number: {number} END | status {response.status_code}")
    return response

@log_time
def main():
    # [call_api(i) for i in range(10)]
    # thread1 = threading.Thread(target=call_api, args=(1,))
    # thread1.start()
    # thread1.join()
    threads = [threading.Thread(target=call_api, args=(i,)) for i in range(10)]
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]


if __name__ == "__main__":
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n")
    main()
    print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")  # noqa: E303
    