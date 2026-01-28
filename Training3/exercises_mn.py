import copy

print("Hello World 1234445567")

g = {"a": 23, "b": 44}
g["c"]=323
print(g)

original = [[1, 2, 3], [4, 5, 6]]
# Shallow copy – only top-level list is copied
shallow = copy.copy(original)
deep = copy.deepcopy(original)

original2 = original

original[0][0] = 999
print(shallow)

original[1] = 888
print(shallow)

original2[1] = 888
print(original2)

d1 = {"a": 333, "b": 9999}
d11, d12 = d1
print(d11, d12)

for k, v in d1.items():
    print(k, v)

a = [1,2,3,4]
print(a[1:2]) # 2
print(a[1:3]) # 2,3


dict = {"a": 434, "b": 789}
for item in dict:
    print(item)


fruits = ["apple", "banana", "cherry"]
print("Using enumerate():")
for index, value in enumerate(fruits):  #0987
    print(index, value)
print(enumerate(fruits))


names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
print("Using zip():")
for name, score in zip(names, scores):
    print(score, name)
print(zip(names, scores))

print("------------------------------")

def funn333(*args, **kwargs):
    for item_a in args:
        print(f"item_a : {item_a}")
    for item_k, item_v in kwargs.items():
        print(f"item_k : {item_k}, item_v: {item_v}")


print("============================")
funn333(1, 3, (32, 43), [989, 898, 323], a=1, b=44)
print("============================")
funn333([9999, 9999, "werwer"], it=32332, dd={"aaa": "aaaa", "bbb": "bbbb"})


print("-----enumerate-------")
# help(enumerate)
li1 = list("abc")
print(li1)
aaa= {}
for indeks, wartosc in enumerate(li1):
    aaa[indeks]=wartosc

print(aaa)

print("-----zip-------")
li2 = list("abc")
li3 = list("45644")
lll = {}
for li2, li3 in zip(li2,li3):
    lll[li2]=li3
print(lll)

print("-----args-------")
def funkcja(*args):
    if isinstance(args[0],list):
        for item22 in args[0]:
            print(item22)
        print("<<<>>>")
    else:
        print(args)

funkcja([1,2,3])
funkcja(9)
funkcja("string")
funkcja({45,67,89})