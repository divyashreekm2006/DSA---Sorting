"""
Problem 8: Count Inversions
Description: Count the pairs where an earlier element is greater than a later element.

Example:

Input: [2, 4, 1, 3, 5]

Output: 3

Explanation: Inversions are (2,1), (4,1) and (4,3).
"""

def count_inversions(arr):

    def merge_sort_count(arr):
        if len(arr) <= 1:
            return arr, 0

        mid = len(arr) // 2

        left, left_count = merge_sort_count(arr[:mid])
        right, right_count = merge_sort_count(arr[mid:])

        merged = []
        i = 0
        j = 0
        count = left_count + right_count

        while i < len(left) and j < len(right):

            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1

            else:
                merged.append(right[j])
                count += len(left) - i
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged, count

    sorted_arr, total = merge_sort_count(arr)

    return total

arr = [2, 4, 1, 3, 5]

result = count_inversions(arr)

print("Number of Inversions:", result)