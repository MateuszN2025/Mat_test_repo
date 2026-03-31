import time

def generator():
    i = 0
    while i<100:
        yield i
        i+=1
        time.sleep(0.1)

gen = generator()

# for item in gen:
#     print(item)


def gen1():
    yield 1
    yield 222
    yield 3333

for i in gen1():
    print(i)


print("##########")

r = 100000

def gen2():
    for i in range(r):
        yield i


start1 = time.time()

for j in gen2():
    print(j)

end1 = time.time()


print("########")

z=0
start2 = time.time()

for z in range(r):
    z+=1
    print(z)

end2 = time.time()

print("########")
print("Czas wykonania generatora:", end1 - start1, "sekundy")
print("Czas wykonania for-a:", end2 - start2, "sekundy")