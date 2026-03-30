try:
    a = 2/1
except (ZeroDivisionError, NameError):
    print("0 error")
else:
    print(f"result: {a}")
finally:
    print("Done anyway")