for i in range(2, 20, 3):
    print(i)



print("===================================")

print([i for i in range(10)])

print("===================================")



a = [123, 2432, 2333, 234, 234]

print([item for item in a if item % 2 == 0])
print("===================================")

b = 19
j = 0
while b > 10:
    print(f"Hi {j}")
    b -= 1
    j += 1

print("===================================")