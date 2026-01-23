a = {}
b = {'a': 1}
print(b)
b["new_key"] = 123
print(b)

for i in range(11):
    b[f"key{i}"] = i

del(b["key4"])

print(b)