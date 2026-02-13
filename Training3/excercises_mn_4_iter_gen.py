print("iterators vs generators – differences and use cases")
"""
✅ Use Iterator when:
You need full control over iteration
Complex state management
Creating reusable iterable objects

✅ Use Generator when:
Working with large datasets
Reading large files
Streaming data
Memory efficiency is important
You want simple, clean code

🚀 Quick Summary
Iterator = Manual implementation of iteration protocol
Generator = Easy way to create iterators using yield
Generators are generally preferred unless you need special behavior
"""
class Iter1:
    def __init__(self, max):
        self.max = max
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter <= self.max:
            self.counter += 1
            return self.counter
        else:
            return StopIteration

it1 = Iter1(5)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))

print("=================")
# Implements __iter__() and __next__() methods
# Produces values one at a time
# Raises StopIteration when finished
list1 = [item for item in range(10,20,2)]
iter1 = iter(list1)

print(next(iter1))
print(next(iter1))
print(next(iter1))

print("=================")
def gen1():
    yield 1
    yield 3
    yield 5

for iii in gen1():
    print(iii)

print("=================")
print("=================")
# This restarts every time:
print(type(gen1()))

print(next(gen1())) # 1
print(next(gen1())) # 1
print("----------------")
# This continues:
# gen1() creates a new generator every time.
# If you want continuation, store it in a variable.
ggg = gen1()

print(type(ggg))
print(next(ggg)) # 1
print(next(ggg)) # 3

print("=================")
print("=================")

"""
Each time you call:
gen1()
you create a brand new generator object.
So this:
next(gen1())
means:
Create new generator
Call next() once
Return first yielded value → 1
Generator is discarded
Then you do it again — creating a new one again — so it starts from the beginning again.
"""

def gen2():
    for item2 in range(30,35,1):
        yield item2

for item3 in gen2():
    print(item3)

print("=================")
for item3 in range(3):
    print(next(gen2()))

print("=================")
def gen():
    yield 1
    yield 2

g = gen()
print(next(g))  # 1
print(next(g))  # 2

