import time

def log(func):
    def wrapper(*args, **kwargs):
        t1 = time.perf_counter_ns()
        result = func(*args, **kwargs)
        t2 = time.perf_counter_ns()
        td = t2 - t1
        print(f"td: {int(td//1e6)} ms")
        return result
    return wrapper


def log_a(func):
    async def wrapper(*args, **kwargs):
        t1 = time.perf_counter_ns()
        result = await func(*args, **kwargs)
        t2 = time.perf_counter_ns()
        td = t2 - t1
        print(f"td: {int(td//1e6)} ms")
        return result
    return wrapper