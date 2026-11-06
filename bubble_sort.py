"""
Problem 1: Bubble Sort
Description: Sort an array in ascending order by repeatedly comparing and swapping adjacent elements.

Example:

Input: [5, 1, 4, 2, 8]

Output: [1, 2, 4, 5, 8]
"""

def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

arr = [5, 1, 4, 2, 8]

result = bubble_sort(arr)

print("Original Array:", arr)
print("Sorted Array:", result)