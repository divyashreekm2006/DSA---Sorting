"""
Problem 13: Minimum Swaps to Sort
Description: Given an array of distinct integers, find the minimum number of swaps required to sort it in ascending order.

Example:

Input: [4, 3, 2, 1]

Output: 2

"""
def minimum_swaps(arr):

    n = len(arr)

    indexed_arr = list(enumerate(arr))

    indexed_arr.sort(key=lambda x: x[1])

    visited = [False] * n

    swaps = 0

    for i in range(n):

        if visited[i] or indexed_arr[i][0] == i:
            continue

        cycle_size = 0
        j = i

        while not visited[j]:

            visited[j] = True

            j = indexed_arr[j][0]

            cycle_size += 1

        if cycle_size > 1:
            swaps += cycle_size - 1

    return swaps

arr = [4, 3, 2, 1]

result = minimum_swaps(arr)

print("Minimum Swaps:", result)