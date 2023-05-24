# Function Description
#
# Complete the insertionSort1 function in the editor below.
#
# insertionSort1 has the following parameter(s):
#
# n: an integer, the size of
# arr: an array of integers to sort
# Returns
#
# None: Print the interim and final arrays, each on a new line. No return value is expected.
# Input Format
#
# The first line contains the integer , the size of the array .
# The next line contains  space-separated integers .
#
# Constraints
#
#
#
# Output Format
#
# Print the array as a row of space-separated integers each time there is a shift or insertion.
#
# Sample Input
#
# 5
# 2 4 6 8 3
# Sample Output
#
# 2 4 6 8 8
# 2 4 6 6 8
# 2 4 4 6 8
# 2 3 4 6 8
# Explanation
#
#  is removed from the end of the array.
# In the st line , so  is shifted one cell to the right.
# In the nd line , so  is shifted one cell to the right.
# In the rd line , so  is shifted one cell to the right.
# In the th line , so  is placed at position .
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    tmp = arr[n-1]
    t = n-2
    while t>=0 and arr[t] > tmp:
        arr[t+1] = arr[t]
        t -= 1
        print(' '.join(map(str,arr)))
    arr[t+1] = tmp
    print(' '.join(map(str,arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
