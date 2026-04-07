username = input("Enetr the user name:")
lu = len(username)

if 0 < lu <= 12:
    print(f"correct amount of chars: {lu}, in the user name [OK]")
else:
    print(f"amount of chars: {lu}, in user name is incorrect [X]")

if username.count(" ") == 0:
    print("user name does not contain space [OK]")
else:
    print("user name does  contain space [X]")


username.isnumeric()