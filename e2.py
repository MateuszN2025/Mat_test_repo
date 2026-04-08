# username = input("Enter the user name:")
username = "Bob "

if not len(username) < 12:
    print("User nam has too many characters [X]")
elif not username.find(" ") == -1:
    print("User name contains spaces [X]")
elif not username.isalpha():
    print("User name contains numbers [X]")
else:
    print("Correct user name [OK]")


# a = "abc"
# print(a.isalpha())
# print(a.find(" "))

# b = 6
#
# if b == 6:
#     print("OK")
# else:
#     print("[X]")