#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    n = int(input().strip())
    for a0 in range(n):
        grade = int(input().strip())

        if(grade < 38):
            print (grade)
        elif(grade % 5 > 2):
            print((grade // 5+1)*5)
        else:
            print(grade)

if __name__ == '__main__':
    fptr = sys.stdout
    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
