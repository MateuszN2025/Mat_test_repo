def f(x):
    x = x + 1 # x = x + 1 creates a NEW integer object 11
    # x now points to new object
    # a still points to old 10
    print("Inside:", x)

a = 10
f(a)
print("Outside:", a)

print("--------------")
def f(lst):
    lst.append(4) # .append() modifies the object in place
    # Both names see the change
    print("Inside:", lst)

a = [1, 2, 3]
f(a)
print("Outside:", a)

# Python
# Pass-by-object-reference

