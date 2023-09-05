# Function Description
#
# Complete the function countSwaps in the editor below.
#
# countSwaps has the following parameter(s):
#
# int a[n]: an array of integers to sort
# Prints
#
# Print the three lines required, then return. No return value is expected.
#
# Input Format
#
# The first line contains an integer, , the size of the array .
# The second line contains  space-separated integers .
#
# Constraints
#
# Output Format
#
# Sample Input 0
#
# STDIN   Function
# -----   --------
# 3       a[] size n = 3
# 1 2 3   a = [1, 2, 3]
# Sample Output 0
#
# Array is sorted in 0 swaps.
# First Element: 1
# Last Element: 3
# Explanation 0
# The array is already sorted, so  swaps take place.
#
# Sample Input 1
#
# 3
# 3 2 1
# Sample Output 1
#
# Array is sorted in 3 swaps.
# First Element: 1
# Last Element: 3
# Explanation 1
# The array is not sorted, and its initial values are: . The following  swaps take place:
#
# At this point the array is sorted and the three lines of output are printed to stdout.
import math
import os
import random
import re
import sys

def countSwaps(a):
    swaps = 0
    n = len(a)

    for i in range(n):
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1

    print("Array is sorted in", swaps, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[-1])

if __name__ == '__main__':
    n = int(input("Enter the number of integers:").strip())
    a = list(map(int, input("Enter the integers separated by spaces:").rstrip().split()))

    countSwaps(a)