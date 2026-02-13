print("data structures: list vs tuple, dictionaries (e.g. printing all keys),")
dict1 = {"a":1, "b":3}
print("-----------")
print(dict1.keys())
print("-----------")
print(dict1.values())
print("-----------")
print(dict1.items())
print("-----------")

a = []
a.append(1)
print(a)
b = [item for item in range(10)]
print(b)
b.insert(2,777)
print(b)
b.pop(10)
print(b)
del b[9]
print(b)
print("=========")
t1 = (4,5,6)
print(t1.count(4))

tt1,tt2,tt3 = t1
print(tt3)
print("=========")
for k,v in dict1.items():
    print(k,v)

print("terators vs generators – differences and use cases,")