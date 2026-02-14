import random

print("-----------------------")
list1 = [1,2,3,4,5,6]
print(list1)
print(random.choice(list1))
print("-----------------------")
tuple1 = (33,44,55,66,77)
print(random.choice(tuple1))
print("-----------------------")
print(random.choice("sasdsadasddddddwiuroiuoi"))
print("-----------------------")
set1 = {3,4,5,6,5,3,2,2,1}
print(set1)
print(random.choice(list(set1)))
print("-----------------------")
dict1 = dict(a=22,b=44,c=55)
print(dict1)
print(random.choices(list(dict1.items())))
print(random.choices(list(dict1.values())))
print("-----------------------")
items = ["apple", "banana", "cherry"]
print(random.sample(items, 2)) # two random elements
print(random.choices(items, k=2))
print("-----------------------")
print(random.randint(10,100))
print(random.randrange(555,999))