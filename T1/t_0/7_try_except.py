try:
    a = 2 / 0
except ZeroDivisionError:
    print("Forbidden")
else:
    print("else")
finally:
    print("Done anyway")