a = [1,2,3]


def func(a: list):
    return [item*2 for item in a]


print(func(a))


b = {"new": 2, "old": 3}

for k,v in b.items():
    print(f"key: {k}, value: {v}")


list1 = [i for i in range(100)]

print("=========")
for i in range(0, 10, 2):
    print(i)

print("=========")

print([item4*4 for item4 in list1 if item4 % 2 == 0])

