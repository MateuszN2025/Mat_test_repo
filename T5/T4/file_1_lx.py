"""
Write a function called interval_intersection(a, b) that takes two 2-element tuples,
a = (start1, end1)
and b = (start2, end2),
representing intervals of integers (inclusive).

The intervals can be given in any order — meaning the start point may be greater than the end point.

Your function should:

Validate each interval: if either interval is invalid (i.e., start > end), return None.
Find the intersection of the two intervals, if any.
Return the intersection as a tuple (start, end).
If the intervals do not overlap, return None.

"""

# przeykład a = (1,2)
# b = (3,4)

def interval_intersection(a, b):
    # (2,8)
    # (4, 10)
    # (4,8)
    c = []

    if (a[0] <= a[1] or b[0] <= b[1]) or ():
        pass
    else:
        print("Start is not less than end")
        return None

    if a[0] < b[0]:
        c.append(b[0])
    else:
        c.append(a[0])

    if a[1] < b[1]:
        c.append(a[1])
    else:
        c.append(b[1])

    return tuple(c)


print(interval_intersection(a=(2,8), b=(4, 10)))
print("================")
print(interval_intersection(a=(5, 5), b=(5, 5)))
print("================")
print(interval_intersection((10, 2), (3, 4)))





