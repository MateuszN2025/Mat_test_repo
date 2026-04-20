
#   [
#       [1,2,3],  i = 0
#       [1,2,3],  i = 1
#       [1,2,3]   i = 2
#   ]

r = 3

# table1 = [None for x in range(r)]
table2 = [None for y in range(r)]

# for i in range(r):
#     for j in range(r):
#         table2[j] = j
#     table1[i] = table2⚠️
#
# print(table1)
#
# table1[0][0] = 99⚠️
# print(table1)

# [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
# [[99⚠️, 1, 2], [99⚠️, 1, 2], [99⚠️, 1, 2]] # ⚠️


r = 3
table1 = [None for _ in range(r)]

for i in range(r):
    # table2 = [None for _ in range(r)]
    table2 = list(None for _ in range(r))
    # table2 = [None for _ in range(r)] creates a
    # completely new list because that expression is evaluated again at that moment,
    # and each evaluation of a list comprehension allocates a fresh list object in memory.
    # ⚠️ does not “clear” or “reuse” the old list. It builds a new one and then ⚠️
    # ⚠️ makes the name table2 point to that new object. ⚠️
    for j in range(r):
        table2[j] = j
    table1[i] = table2

print(table1)

table1[0][0] = 99
print(table1)

# r = 3
# table1 = [[j for j in range(r)] for _ in range(r)]
# print(table1)


"""
r = 3

a = [None for _ in range(r)]
b = list(None for _ in range(r))
c = [None] * r

print(a)  # [None, None, None]
print(b)  # [None, None, None]
print(c)  # [None, None, None]
"""
print("------------------------------------------")
a = [1, 2, 3]
b = a
b[0] = 99
print("a = ", a)   # [99, 2, 3]
print("b = ", b)   # [99, 2, 3]
# Because both names point to the same object.
print("a is b",a is b)
print("------------------------------------------")
a = [1, 2, 3]
b = a.copy() # ⚠️
b[0] = 99

print("a = ", a)   # [1, 2, 3]
print("b = ", b)   # [99, 2, 3]
print("a is b",a is b)

print("------------------------------------------")
a = [1, 2]
b = a
print("a",a)
print("b",b)
a = [9, 9]
print("a",a)
print("b",b)