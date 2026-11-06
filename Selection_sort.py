"""
Problem 3: Selection Sort
Description: Sort an array by repeatedly selecting the smallest element from the unsorted portion.

Example:

Input: [64, 25, 12, 22, 11]

Output: [11, 12, 22, 25, 64]
"""

def selection_sort(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

arr = [64, 25, 12, 22, 11]

result = selection_sort(arr)

print("Original Array:", arr)
print("Sorted Array:", result)