"""
Problem 15: Merge Sort
Description: Sort an array using the Merge Sort algorithm by dividing it into smaller arrays and merging them in sorted order.

Example:

Input: [38, 27, 43, 3, 9, 82, 10]

Output: [3, 9, 10, 27, 38, 43, 82]
"""
def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):

    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

arr = [38, 27, 43, 3, 9, 82, 10]

result = merge_sort(arr)

print("Original Array:", arr)
print("Sorted Array:", result)