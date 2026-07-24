def missing_number(nums, n):
    # Expected sum of numbers from 1 to n using formula:
    # 1 + 2 + ... + n = n * (n + 1) // 2
    expected_sum = n * (n + 1) // 2

    # Actual sum of values present in the input list.
    actual_sum = sum(nums)

    # The difference is the missing number.
    return expected_sum - actual_sum


# Example list has numbers from 1..5, but one value is missing.
nums = [1, 2, 3, 5]

# Missing value is 4.
print(missing_number(nums, 5))

