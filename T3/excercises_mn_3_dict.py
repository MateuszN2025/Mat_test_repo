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

print("=====unpack dict====")
dict1 = dict(a=1,b=3,c=4)
print(dict1)
# WRONG !
# dict2 = dict("3"=1,"s"=3,"4"=4)
# print(dict2)

k1, k2, k3 = dict1.keys()
print(k1, k2, k3)
v1, v2, v3 = dict1.values()
print(v1, v2, v3)
k1v1, k2v2, k3v3 = dict1.items()
print(k1v1, k2v2, k3v3)

