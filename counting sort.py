#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    freq = [0] * 100  # Assuming you're counting numbers from 0 to 99
    for i in arr:
        freq[i] = freq[i] + 1
    return freq

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    # Print the result, which is the frequency count of numbers
    print(' '.join(map(str, result)))