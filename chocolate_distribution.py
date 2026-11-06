"""
Problem 5: Chocolate Distribution Problem
Description: Given chocolate packets and M students, distribute one packet to each student so that the difference between maximum and minimum chocolates is minimum.

Example:

Input: ([7, 3, 2, 4, 9, 12, 56], 3)

Output: 2

Explanation: Select packets [2, 3, 4]. Difference = 4 - 2 = 2.
"""

def chocolate_distribution(arr, m):
    n = len(arr)

    if m <= 0 or m > n:
        return -1

    arr = sorted(arr)
    min_diff = float('inf')

    for i in range(n - m + 1):
        diff = arr[i + m - 1] - arr[i]

        if diff < min_diff:
            min_diff = diff

    return min_diff

arr = [7, 3, 2, 4, 9, 12, 56]
m = 3

result = chocolate_distribution(arr, m)

print("Minimum Difference:", result)