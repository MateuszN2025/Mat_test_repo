def twoSum(nums, target):
    # Create a dictionary to store complement values
    complement_dict = {}

    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement needed to reach the target
        complement = target - num

        # Check if the complement exists in the dictionary
        if complement in complement_dict:
            # Return the indices of the two numbers
            return [complement_dict[complement], i]

        # Store the current number and its index in the dictionary
        complement_dict[num] = i

    # If no solution is found
    return []

# Example 1
nums1 = [2, 7, 11, 15]
target1 = 9
print(twoSum(nums1, target1))  # Output: [0, 1]

# Example 2
nums2 = [3, 2, 4]
target2 = 6
print(twoSum(nums2, target2))  # Output: [1, 2]

# Example 3
nums3 = [3, 3]
target3 = 6
print(twoSum(nums3, target3))  # Output: [0, 1]