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
def funkcja_args(*args):
    # print("====")
    # print(args)
    # print("====")
    if isinstance(args[0],list):
        for item22 in args[0]:
            print(item22)
        print("<<<>>>")
    else:
        print(args)

funkcja_args([1,2,3])
funkcja_args(9)
funkcja_args("string")
funkcja_args({45,67,89})


print("-------------lambda & map-----------------")
kwadracik = lambda x: x**2
li4 = list((1,3,4,5))
print(li4)
li5 = list(map(kwadracik, li4))
print(li5)


print("------------kwargs------------------")
def funkcja_kwargs(**kwargs):
    print(kwargs)

funkcja_kwargs(a=1)
funkcja_kwargs(b=5,c=[1,3])
funkcja_kwargs(s='sss', a={"a":1})

"""
| *args               | **kwargs          |
| ------------------- | ----------------- |
| tuple               | dict              |
| argumenty pozycyjne | argumenty nazwane |
| `f(1,2,3)`          | `f(a=1,b=2)`      |
"""

print("------------args + kwargs------------------")
def funkcja_a_k(*args, **kwargs):
    print(f"to jest args: {args}")
    print(f"to jest kwargs: {kwargs}")

funkcja_a_k(3,'sf',[3,'s'],a=2, bb={"dd":2343})
funkcja_a_k(3, bb={"dd":2343})

"""
def create_user(username, *groups, **options):
    print("Username:", username)
    print("Groups:", groups)
    print("Options:", options)

create_user(
    "mateusz",
    "admin", "dev",
    active=True,
    email="mateusz@test.com"
)
"""