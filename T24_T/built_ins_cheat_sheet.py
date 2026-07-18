
nums = [5, 2, 9, 1]

print(min(nums))
print(max(nums))
print(sum(nums))
print(len(nums))

# enumerate: index + value
indexed = list(enumerate(["a", "b", "c"], start=1))
print(indexed)

# zip: pair elements by position
paired = list(zip(["T1", "T2"], ["PASS", "FAIL"]))
print(paired)