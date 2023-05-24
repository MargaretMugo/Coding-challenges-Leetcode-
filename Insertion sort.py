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
