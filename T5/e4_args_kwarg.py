# add_numbers(1,2,3) → inside function: args = (1,2,3)
# add_numbers([1,2]) → inside function: args = ([1,2],)
# name="Alice", age=25 → inside function: kwargs = {'name':'Alice', 'age':25}

dict1 = dict(a=1,b=2)
print(dict1)
# k,v = **dict1
# ** is used for unpacking dictionaries in function calls, not in assignments.


for k, v in dict1.items():
    print(k, v)

print("==========")
def my_func(a, b):
    print(a, b)

my_func(**dict1)  # a=1, b=2
print("==========")

'''
def my_func(a, b):
    print(a, b)

dict1 = {'a': 1, 'b': 2}
my_func(**dict1)

What happens:

    **dict1 transforms the dictionary into keyword arguments:

my_func(a=1, b=2)
'''
# 2️⃣ Important: Keys must match parameter names
