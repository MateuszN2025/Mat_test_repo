import os
import subprocess
import inspect
import math
subprocess.run(args="clear")



print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n")

def cosik() -> str:
    print("cosik")
    return "cosik"

class Klasik:
    pass


print("-------------------os.__file__-----------------------")
print(f"{os.__file__}")
print("-------------------inspect.getfile-----------------------")
print(f"{inspect.getfile(cosik)}")
print("-------------------inspect.getsource-----------------------")
print(f"{inspect.getsource(cosik)}")
print("------------------- __annotations__ -----------------------")
print(f"{(cosik.__annotations__)}")
print("-------------------dir-----------------------")
print(f"{dir(cosik)}")
print("-------------------class-----------------------")
print(f"{dir(Klasik)}")
print("-------------------type-----------------------")
print(f"{type(Klasik)}")
print("-------------------help-----------------------")
print(f"{help(math)}")
print("-------------------__doc__-----------------------")
print(f"{Klasik.__dict__}")


















print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
