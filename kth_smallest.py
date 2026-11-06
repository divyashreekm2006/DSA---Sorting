"""
Problem 7: Kth Smallest Element
Description: Given an array and an integer K, find the Kth smallest element. Duplicate values are counted separately.

Example:

Input: ([7, 10, 4, 3, 20, 15], 3)

Output: 7
"""

def kth_smallest(arr, k):

    if k < 1 or k > len(arr):
        return None

    sorted_arr = sorted(arr)

    return sorted_arr[k - 1]

arr = [7, 10, 4, 3, 20, 15]
k = 3

result = kth_smallest(arr, k)

print("Kth Smallest Element:", result)