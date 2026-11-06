"""
Problem 9: Wave Array
Description: Rearrange an array into wave form:

arr[0] >= arr[1] <= arr[2] >= arr[3] ...

Example:

Input: [1, 2, 3, 4, 5]

Output: [2, 1, 4, 3, 5]
"""

def wave_array(arr):
    arr = sorted(arr)

    for i in range(0, len(arr) - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return arr


arr = [1, 2, 3, 4, 5]

result = wave_array(arr)

print("Wave Array:", result)