print("iterators vs generators – differences and use cases")

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

print(next(gen1()))
print(next(gen1()))
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

print("=================")


