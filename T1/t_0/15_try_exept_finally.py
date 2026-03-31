try:
    a = "a"/1
except (ZeroDivisionError, NameError, TypeError) as e:
    print(f"this is e : {e}")
else:
    print(f"result: {a}")
finally:
    print("Done anyway")