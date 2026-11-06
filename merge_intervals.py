"""
Problem 12: Merge Overlapping Intervals
Description: Given a collection of intervals, merge all overlapping intervals.

Example:

Input: [[1, 3], [2, 6], [8, 10], [15, 18]]

Output: [[1, 6], [8, 10], [15, 18]]
"""

def merge_intervals(intervals):

    if not intervals:
        return []

    intervals = sorted(intervals)

    result = [intervals[0]]

    for current in intervals[1:]:

        last = result[-1]

        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])

        else:
            result.append(current.copy())

    return result

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

result = merge_intervals(intervals)

print("Merged Intervals:", result)