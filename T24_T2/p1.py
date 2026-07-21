print("------------------------------------------")
# enumerate: index + value
indexed = list(enumerate(["a", "b", "c"], start=1))
print(indexed)
print("------------------------------------------")
# zip: pair elements by position
paired = list(zip(["T1", "T2"], ["PASS", "FAIL"]))
print(paired)
print("------------------------------------------")
s = lambda x: x**2
l1 = [1, 2, 3]
print(list(map(s, l1)))
print("------------------------------------------")
dict1 = {"a":1}
dict2 = {"b":2}
# print({**dict1, **dict2})
print(dict1 | dict2)