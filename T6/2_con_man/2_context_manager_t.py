# import json
# with open("1_win_logs.txt") as f:
#     file = f
#     # print(file)
#     # print(file.readline())
#     # print(file.readlines())
#     # print(type(file.readlines()))
#     list1 = file.readlines()
#
# print(list1)
# json_formatted_string = json.dumps(list1)
# print(json_formatted_string)
# print(type(json_formatted_string))
import contextlib
# class Cont_man:
#     def __init__(self, file_name):
#         self.file_name = file_name
#
#     def __enter__(self):
#         self.file = open(self.file_name, "r")
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
#
#
# cm = Cont_man("2_win_logs.txt")
# with cm as f:
#     f.readlines()

# class Cont_man2:
#     def __init__(self, file_name):
#         self.file_name = file_name
#         self.file = None
#
#     def __enter__(self):
#         self.file = open(self.file_name, "r")
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self.file and not self.file.closed:
#             # print(type(self.file_name))
#             # print(f"file: {self.file},\nstatus: {self.file.closed}")
#             self.file.close()
#         return False
#
#     def __str__(self):
#         return "<<<>>>"
#
# cm2 = Cont_man2("2_win_logs.txt")
# with cm2 as f:
#     # print(f.readlines())
#     f.__str__()
#     cm2.__str__()
#     print(f.__str__())
#     print(cm2.__str__())


# from contextlib import contextmanager
#
# @contextmanager
# def cont_man_3(file_name):
#     print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#     print(f"opening the file: {file_name}")
#     file3 = open(file_name, "r")
#     try:
#         yield file3
#     finally:
#         print("closing the file")
#         file3.close()
#         print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#
# with cont_man_3("2_win_logs.txt") as f3:
#     print("===========")
#     print(f3)
#     print(f3.readline())
#     print("===========")

# class Ctx:
#     def __enter__(self):
#         print(">>> enter <<<")
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("exc_type:", exc_type)
#         print("exc_val:", exc_val)
#         print("exc_tb:", exc_tb)
#         return False
#
# with Ctx():
#     try:
#         print(type("a"/0))
#         print(1/3)
#     except Exception as e:
#         print("---")
#         print("1/0")
#         print(e)
#         print("---")
#     else:
#         pass
#     finally:
#         pass

# >>> enter <<<
# exc_type: <class 'ZeroDivisionError'>
# exc_val: division by zero
# exc_tb: <traceback object at 0x0000014EB7135080>

print("========================Con_Man_4_time_measure==============================")

import time

class Con_Man_4_time_measure:
    def __init__(self, func):
        self.t1 = 0
        self.t2 = 0
        self.td = 0
        self.func = func

    def __enter__(self):
        self.t1 = time.time()
        print(f"Enter the block of code. Time is: {self.t1}")
        print("-----------------")
        self.func()
        return self.func.__name__ # <=============

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.t2 = time.time()
        print("-----------------")
        print(f"Exit the block of code. Time is: {self.t2}")
        self.td = self.t2 - self.t1
        print(f"Time difference is {self.td}")

def for_loop_xxxx():
    for item in range(100000000):
        pass


cm4 = Con_Man_4_time_measure(for_loop_xxxx)

with cm4 as ccc:
    print(ccc)

print("========================cont_man_5==============================")

@contextlib.contextmanager
def cont_man_5(func_5):
    t1 = time.time()
    print(f"Enter the block of code. Time is: {t1}")
    print("-----------------")
    func_5()
    yield func_5.__name__ # <=============
    t2 = time.time()
    print("-----------------")
    print(f"Exit the block of code. Time is: {t2}")
    td = t2 - t1
    print(f"Time difference is {td}")

with cont_man_5(for_loop_xxxx) as cm5:
    print(cm5)


















