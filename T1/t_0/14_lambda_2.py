suma = lambda x, y: x + y

print(suma(3,4))
print("-------")
s = lambda x: f"this is {x}"
l1 = [33,44,55]
l2 = list(map(s,l1))
print("-------")
print(l2)
print("-------")
print(print("a"))
print("============")
people = [
    {'name': 'Anna', 'age': 25},
    {'name': 'Jan', 'age': 30},
    {'name': 'Ola', 'age': 20}
]
sorted_people = sorted(people, key=lambda p: p["age"])
# p gets its value because sorted() passes each element of people into the lambda.
print(people)
print(f"sorted people: {sorted_people}")
print("============")
print(list(sorted_people))
