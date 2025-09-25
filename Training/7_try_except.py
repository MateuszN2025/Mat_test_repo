try:
    a = 2 / 3
except ZeroDivisionError:
    print("Forbidden")
finally:
    print("Done anyway")