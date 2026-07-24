def find_duplicates(nums):
    seen = set()
    duplicates = set()

    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)


nums = [1, 2, 3, 4, 2, 5, 6, 3]
print(find_duplicates(nums))