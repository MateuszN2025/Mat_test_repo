from contextlib import contextmanager
import time

# @contextmanager
# def comments():
#     value = 123
#     print(f"start time: {time.time()}")
#     yield print("running"), value
#     print(f"end time: {time.time()}")
# comments return: (None, 123)

@contextmanager
def comments():
    value123 = 123
    print(f"start time: {time.time()}")
    print("running")
    yield value123
    print(f"end time: {time.time()}")


if __name__ == '__main__':

    list1 = []
    with comments() as c:
        # Everything inside the yield expression is evaluated before the with block runs.
        for item in range(10000000):
            list1.append(item)
        print(list1[len(list1)-1])
    print(c) # return value123 



'''
Without context manager:

f = open("data.txt")
try:
    data = f.read()
finally:
    f.close()
    
With context manager:

with open("data.txt") as f:
    data = f.read()
    
The file always closes, even if an exception occurs.
'''

# 🔹 Why Context Managers Are Important
# # They guarantee:
# # ✅ Automatic cleanup
# ✅ Cleaner code
# ✅ Exception safety
# ✅ Resource management