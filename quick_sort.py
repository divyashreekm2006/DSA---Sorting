"""
Problem 14: Quick Sort
Description: Sort an array using the Quick Sort algorithm by selecting a pivot and partitioning the array.

Example:

Input: [10, 7, 8, 9, 1, 5]

Output: [1, 5, 7, 8, 9, 10]
"""

def quick_sort(arr):

    arr = arr.copy()

    def partition(low, high):

        pivot = arr[high]
        i = low - 1

        for j in range(low, high):

            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        return i + 1

    def sort(low, high):

        if low < high:

            pivot_index = partition(low, high)

            sort(low, pivot_index - 1)
            sort(pivot_index + 1, high)

    sort(0, len(arr) - 1)

    return arr

arr = [10, 7, 8, 9, 1, 5]

result = quick_sort(arr)

print("Sorted Array:", result)