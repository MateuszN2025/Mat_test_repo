# # a.1. make a gen with a for loop
# print("===== gen1 =======")
# def gen1():
#     for item1 in range(5,16):
#         yield item1
#
# g1 = gen1()
#
# #  StopIteration
# # for item11 in range(20):
# #     print(item11, next(g1))
#
# for item11 in g1:
#     print(item11)
#
# # a.2. make a iter with a for loop
# print("===== Iter1 =======")
# class Iter1:
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop
#         self.counter = 0
#
#     def __iter__(self):
#         """
#         Pattern B: Object creates iterator
#             def __iter__(self):
#                 return NewIterator(...)
#         """
#         # return Iter1(self.start, self.stop)
#         """
#         Pattern A: Object is the iterator
#             def __iter__(self):
#                 return self
#         """
#         return self
#
#
#     def __next__(self):
#         if self.start <= self.stop:
#             self.counter = self.start
#         else:
#             raise StopIteration
#         self.start += 1
#         return self.counter
#
# print("-------Iter1 StopIteration----------")
# i1 = Iter1(5,15)
# # for item111 in range(20):
# #     print(item111,next(i1))
# print("------Iter1-----------")
# for item111 in i1:
#     print(item111)
# print("------Iter1-----------")
# for item111 in i1:
#     print(item111)

















# # b.1 make a gen to open file
# print("============")
#
# def gen2(file_name):
#     with open(file_name, "r") as f:
#         for line in f:
#             yield line
#
# g2 = gen2("win_logs.txt")
# print(next(g2))
# print("============")
# for i, j in enumerate(g2):
#     print(i, j)
# # print(next(g2))
# # print(next(g2))




























# b.2 make a iter to open a file
# print("=====Iter 2=======")
#
# class Iter2:
#     def __init__(self, file_name):
#         self.file = open(file_name, "r")
#     def __iter__(self):
#         return self
#     def __next__(self):
#         line = self.file.readline()
#         if line == "":
#             raise StopIteration
#         return line
#
# i2 = Iter2("win_logs.txt")
#
#
# print("=====Iter 2=======")
# print(next(i2))
# print(next(i2))
#
# # for z in range(100):
# #     print(z,next(i2))
#
# print("=====Iter 2=======")
# for y in i2:
#     print(next(i2))

print("=====Iter 3=======")
class Iter3:
    def __init__(self, file_name):
         # with open(file_name, "r") as f:
         #     self.file = f
         """
                             line = self.file.readline()
                         ValueError: I/O operation on closed file.
         """
         #  The commented with block fails for a precise reason:
         #  the file is closed before next ever runs.

         f = open(file_name, "r")
         self.file = f

    def __iter__(self):
        return self
    def __next__(self):
        line = self.file.readline()
        if line == "":
            # self.file.close() # can be here
            raise StopIteration
        else:
            return line

    def close(self):
        if not self.file.closed:
            self.file.close()

i3 = Iter3("win_logs.txt")

print(next(i3))
print(next(i3))

for item3 in i3:
    print(next(i3))

i3.close()

