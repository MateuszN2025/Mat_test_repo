print([item**2 for item in range(0,10,2) if item >= 3])
sum = lambda x,y: x+y
print(sum(3,4))
s=sum(3,4)
print("#######")
li = []
for i in range(30):
    if i%2==0:
      li.append(i)
print(li)
print("#######")
print(li[:2])
print(li[2:5])
print("#######")
print(len(li))
print(min(li))
print(max(li))
print(sorted(li, reverse=True))
li_s = "abc"
print(list(li_s))
# any(lista)	True, jeśli dowolny element jest prawdziwy	any([0,1,0]) → True
# all(lista)	True, jeśli wszystkie elementy są prawdziwe	all([1,2,3]) → True
# kolejne tematy do poczytania to extend, 

