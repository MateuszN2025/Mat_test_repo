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
    lst.append(4) # mutate
    # .append() modifies the object in place
    # Both names see the change

    # lst = [9,9,9] # rebind
    print("Inside:", lst)

a = [1, 2, 3]
f(a)
print("Outside:", a)

# Python
# Pass-by-object-reference

'''
Mutate
Before: my_list ───► [1,2,3]
lst ───┘
lst.append(4)
After:  my_list ───► [1,2,3,4]

Rebind
Before: my_list ───► [1,2,3]
lst ───┘
lst = [9,9,9]  # new object !!!!!!!!!!
After:  my_list ───► [1,2,3]   # unchanged
        lst ───► [9,9,9]
'''

# Immutable objects (int, str, tuple) cannot be mutated
# So for immutables, every operation is rebinding.
print("------------")
def f(s):
    s += " world"   # rebinding

text = "hello"
f(text)
print(text)
