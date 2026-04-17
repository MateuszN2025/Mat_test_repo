import os, inspect, io
# os.rename("7_file1.txt", "7_filee1.txt")


# list1 = [item for item in range(100)]
list1 = []
f = None
i = 0

for item in range(51):
    item = str(item)
    item += " "
    if i % 10 == 0 and i != 0:
        item += "\n"
    list1.append(item)
    i += 1

sss1 = "asdl;askda;lsdk\nl;sfakdl;kfsd;lk"
sss2 = "asdl;askda;lsdkl;sfakdl;kfsd;lk"

# try:
#     f = open("7_file1.txt", "w")
#     # list1_str = str(list1)
#     # print(list1_str)
#     # print(list1_str[2])
#     # # f.writelines("x","\n")
#     # print(help(f.writelines)) # help(io.TextIOBase.writelines)
#     # f.write(str(list1))
#     f.writelines(list1)
#     # print(dir(f.writelines))
#     # print(f.writelines.__doc__)
#
# except FileNotFoundError:
#     print("File Not Found")
# finally:
#     f.close()

# with open("7_fileee1.txt", "r") as f:
#     f.writelines(list1)

try:
    with open("7_filee1.txt", "r") as f:
        # f.writelines(list1)
        print("")
        print(f.read())
except FileNotFoundError as e:
    print(f" >>> {e}")
except OSError as e:
    print(f" >>> >>> {e}")
finally:
    print("if exeption occurs program will move on")

print("1111111111")

# def helpik():
#     """
#     helpik
#     :return:
#     """
#     pass
# print("------------------------------------------")
# print(" __doc__ ------------------------")
# print("------------------------------------------")
# print(io.TextIOBase.writelines.__doc__)
# print("------------------------------------------")
# print(" dir ----------------------")
# print("------------------------------------------")
# print(dir(io.TextIOBase.writelines))
# print("------------------------------------------")
# print(" inspect.getsource helpik -----------------------")
# print("------------------------------------------")
# print(inspect.getsource(helpik))
# print("------------------------------------------")
# print(" inspect.getfile helpik----------------------")
# print("------------------------------------------")
# print(inspect.getfile(helpik))
# print("------------------------------------------")
# print(" os.__file__ ----------------------")
# print("------------------------------------------")
# print(os.__file__) # Shows where the module is located on disk.
# print("------------------------------------------")
# print(" help writelines---------------------")
# print("------------------------------------------")
# # io.TextIOBase.writelines is a built-in method descriptor implemented in C
# # print("inspect.getfile() works for Python objects that come from a source file")
# # TypeError: module, class, method, function, traceback, frame, or code object was expected, got method_descriptor
# # print(inspect.getfile(io.TextIOBase.writelines))
# help(io.TextIOBase.writelines)
# print("------------------------------------------")
# print(inspect.getfile(io))