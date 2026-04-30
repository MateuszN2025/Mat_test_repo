# class Conman:
#
#     def __init__(self, file_name):
#         self.file_name = file_name
#         self.file = None
#
#     def __enter__(self):
#         try:
#             self.file = open(self.file_name, "r")
#         except FileNotFoundError as e:
#             print(f"{e}")
#             raise
#             # FileNotFoundError: [Errno 2] No such file or directory:
#             # '2_win_lo2gs.txt'
#         else:
#             print("File is correct.")
#         finally:
#             print("Process ended.")
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self.file and not self.file.closed:
#             self.file.close()
#
# cm = Conman("2_win_lo2gs.txt")
# with cm as f:
#     print(f.readline())


from contextlib import contextmanager


@contextmanager
def conman2(file_name):
    file = open(file_name, encoding="utf-8")
    print("file opening")
    try:
        yield file
    finally:
        print("file closing")
        file.close()


with conman2("2_win_logs.txt") as ff1:
    print(ff1.readline())






































































































