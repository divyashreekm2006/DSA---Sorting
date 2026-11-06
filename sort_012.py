"""
Problem 6: Sort an Array of 0s, 1s and 2s
Description: Sort an array containing only 0, 1 and 2 without using built-in sorting.

Example:

Input: [0, 2, 1, 2, 0, 1, 0]

Output: [0, 0, 0, 1, 1, 2, 2]
"""

def sort_012(arr):
    arr = arr.copy()

    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:

        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1

        elif arr[mid] == 1:
            mid += 1

        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr

arr = [0, 2, 1, 2, 0, 1, 0]

result = sort_012(arr)

print("Sorted Array:", result)