a = [1, 22, 332, 32, 22324, 4, 4]
print(sorted(a, reverse = True))
# print(a.remove(33)) #  x not in list
# print(a)
print("===================================")
a.remove(22)
print("===================================")
print(a)

print(a.append(43022034))
print(a)

print("===================================")

people = [
    {'name': 'Anna', 'age': 25},
    {'name': 'Jan', 'age': 30},
    {'name': 'Ola', 'age': 20}
]

# Sortowanie po wieku
sorted_by_age = sorted(people, key=lambda x: x['age'])
print(sorted_by_age)

# Sortowanie po nazwie
sorted_by_name = sorted(people, key=lambda x: x['name'])
print(sorted_by_name)

print("===================================")
a = 'yert'
print(''.join([item for item in sorted(a, reverse=True)]))