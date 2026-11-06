"""
Problem 4: Sort a String
Description: Given a string, arrange its characters in alphabetical order.

Example:

Input: "geeks"

Output: "eegks"
"""

def sort_string(s):
    result = ''.join(sorted(s))
    return result

s = "geeks"

result = sort_string(s)

print("Original String:", s)
print("Sorted String:", result)