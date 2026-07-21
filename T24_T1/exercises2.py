dict1 = {"a": 1, "b": 2, "c": 3}

# print(dict1["a"])
# print(list(dict1.keys()))
# print(dir(dict1))

# def reverse_dict(d1: dict) -> dict:
#     pass

list1 = [99,3,4,2,2,1,2,77]
ll1 = len(list1)
list2 = []

for i in range(ll1):
    list2.append(list1[ll1-1])
    ll1 -= 1


# Simplest — slice with negative step
list2 = list1[::-1]

# Using reversed()
list2 = list(reversed(list1))

# Using sorted() with reverse
list2 = sorted(list1, reverse=True)  # sorts + reverses

# Using a loop more idiomatically
list2 = []
for i in range(len(list1) - 1, -1, -1):
    list2.append(list1[i])
    
# print(list2)
print("------------------------------------------")
print(dict1)
print("------------------------------------------")
print({v: k for k, v in dict1.items()})
print("------------------------------------------")
dict2 = {}
for k, v in dict1.items():
    dict2[v] = k

print(dict2)

dict1.update(dict2)
print(dict1)

# merging dicts
# Option 1: Update in-place, then print
dict1.update(dict2)
print(dict1)

# Option 2: Merge into a new dict (keep originals unchanged)
merged = {**dict1, **dict2}  # Python 3.5+
print(merged)

# Option 4: Using | operator (Python 3.9+)
merged = dict1 | dict2
print(merged)