"""
Problem 11: Merge Two Sorted Arrays Without Extra Space
Description: Given two sorted arrays, merge them while maintaining sorted order without creating another array.

Example:

Input:
arr1 = [1, 5, 9, 10]
arr2 = [2, 3, 8, 13]


Output:
arr1 = [1, 2, 3, 5]
arr2 = [8, 9, 10, 13]
"""

def merge_without_extra_space(arr1, arr2):

    n = len(arr1)
    m = len(arr2)

    gap = (n + m + 1) // 2

    while gap > 0:

        i = 0

        while i + gap < n + m:

            j = i + gap

            if i < n and j < n:

                if arr1[i] > arr1[j]:
                    arr1[i], arr1[j] = arr1[j], arr1[i]

            elif i < n and j >= n:

                if arr1[i] > arr2[j - n]:
                    arr1[i], arr2[j - n] = arr2[j - n], arr1[i]

            else:

                if arr2[i - n] > arr2[j - n]:
                    arr2[i - n], arr2[j - n] = (
                        arr2[j - n], arr2[i - n]
                    )

            i += 1

        if gap == 1:
            break

        gap = (gap + 1) // 2

    return arr1, arr2

arr1 = [1, 5, 9, 10]
arr2 = [2, 3, 8, 13]

result1, result2 = merge_without_extra_space(arr1, arr2)

print("First Array:", result1)
print("Second Array:", result2)