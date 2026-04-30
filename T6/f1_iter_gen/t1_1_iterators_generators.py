import time

def gen1():
    yield 1
    yield 22
    yield 333

def gen2():
    for i1 in range(10):
        yield i1

for item1 in gen1():
    print(item1)

print("----------------")

for item2 in gen2():
    if item2 < 130:
        print(item2)

print("----------------")


def gen3(file_name):
    with open(file_name, "r", encoding="utf-8") as f1:
        for line_num, line1 in enumerate(f1, start=1):
            if line_num < 6:
                yield line_num, line1
                # return line_num, line1
                # ----------------
                # (1, '\ufeffLevel\tDate and Time\tSource\tEvent ID\tTask Category\n')
                # Traceback (most recent call last):
                #   File "C:\Users\mniedziolka\PycharmProjects\Mat_test_repo\T6\1_iterators_generators_t.py", line 38, in <module>
                #     for iii1, jjj1 in p1:
                # TypeError: cannot unpack non-iterable int object


# for ln, l1 in gen3("1_win_logs.txt"):
#     print(ln, l1)


p1 = gen3("1_win_logs.txt")
print(p1) # <generator object gen3 at 0x00000243D3B62580>
# for iii1, jjj1 in p1:
#     print(iii1, jjj1)
print(next(p1))
print(next(p1))

print("----------------")


class Iter:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step
        self.list1 = []

        for item in range(self.start, self.stop, self.step):
            self.list1.append(item)

        self.index = 0  # track position

    def __iter__(self):
        """
        ✅ Better design: return a NEW iterator
        Instead, __iter__ should create a fresh iterator:
        def __iter__(self):
            return Iter(self.start, self.stop, self.step)
        """
        return self


    def __next__(self):
        if self.index <= len(self.list1):
            value = self.list1[self.index]
            self.index += 1
        else:
            raise StopIteration
        return value


    def __str__(self):
        return f"start:{self.start}\nstop:{self.stop}\nstep:{self.step}"

i1 = Iter(1,10,2)
print("................")
print(i1.list1)
print("................")
print(next(i1))
print(next(i1))
print(next(i1))
print(next(i1))
print(next(i1))
# print(next(i1)) #IndexError: list index out of range




print("*****************")



# class IterFile:
#     def __init__(self, file_name):
#         self.file_name = file_name
#         self.f2_index = 0
#         self.f2_file = open(file_name, encoding="utf-8")
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         f2_line = self.f2_file.readline()
#         if not f2_line:
#             self.f2_file.close()
#             raise StopIteration
#         return f2_line
#
#
# it_f2 = IterFile("1_win_logs.txt")
# print(next(it_f2).rstrip())
# print(next(it_f2).rstrip('\n'))


class IterFile:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file_obj = None
        self.line_number = 0

    def __iter__(self):
        self.file_obj = open(self.file_name, encoding="utf-8")
        self.line_number = 0
        return self

    def __next__(self):
        if self.file_obj is None:
            self.file_obj = open(self.file_name, encoding="utf-8")

        line = self.file_obj.readline()
        if not line:
            self.file_obj.close()
            self.file_obj = None
            raise StopIteration

        self.line_number += 1
        return self.line_number, line



it_f2 = IterFile("1_win_logs.txt")
print(next(it_f2))
print(next(it_f2))













