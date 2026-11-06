"""
Problem 2: Insertion Sort
Description: Sort an array by inserting each element into its correct position in the sorted portion.

Example:

Input: [12, 11, 13, 5, 6]

Output: [5, 6, 11, 12, 13]
"""

def insertion_sort(arr):
    arr = arr.copy()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

arr = [12, 11, 13, 5, 6]

result = insertion_sort(arr)

print("Original Array:", arr)
print("Sorted Array:", result)