"""
Problem 10: Form the Largest Number
Description: Given a list of non-negative integers, arrange them to form the largest possible number.

Example:

Input: [3, 30, 34, 5, 9]

Output: "9534330"
"""

from functools import cmp_to_key


def largest_number(arr):

    nums = list(map(str, arr))

    def compare(a, b):
        if a + b > b + a:
            return -1
        elif a + b < b + a:
            return 1
        return 0

    nums.sort(key=cmp_to_key(compare))

    result = ''.join(nums)

    if result[0] == '0':
        return '0'

    return result

arr = [3, 30, 34, 5, 9]

result = largest_number(arr)

print("Largest Number:", result)