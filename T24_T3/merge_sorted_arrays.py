def merge_sorted_arrays(arr1, arr2):
    # i points to the current element in arr1
    # j points to the current element in arr2
    # Both start at 0 (the first element).
    i = j = 0

    # This will store the merged, sorted output.
    result = []
    
    """
    # Keep looping while BOTH arrays still have elements left to compare.
    # If either array is fully consumed, we stop this loop and append the rest later.
    
    while i < len(arr1) and j < len(arr2):
        # Compare the current elements from each array.
        # Add the smaller one to result, then move that array's pointer forward.
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    """

    # Iterate a maximum of len(arr1) + len(arr2) times.
    # We break early when one array is exhausted, then append leftovers.
    for _ in range(len(arr1) + len(arr2)):
        if i >= len(arr1) or j >= len(arr2):
            break
        # Compare the current elements from each array.
        # Add the smaller one to result, then move that array's pointer forward.
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    # At this point, at least one array is exhausted.
    # Add any remaining elements from arr1 (if i has not reached the end).
    result.extend(arr1[i:])

    # Add any remaining elements from arr2 (if j has not reached the end).
    result.extend(arr2[j:])

    # Return the fully merged sorted list.
    return result


# Example input: two already-sorted lists
a = [1, 3, 5, 7]
b = [2, 4, 6, 8]

# Expected output: [1, 2, 3, 4, 5, 6, 7, 8]
print(merge_sorted_arrays(a, b))