#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    # Write your code here

    ROWS, COLS = len(matrix), len(matrix[0])
    ans = 0
    for r in range(ROWS//2):
        for c in range(COLS//2):
            ans += max( 
                matrix[r][c],
                matrix[ROWS-1-r][c],
                matrix[r][COLS-1-c],
                matrix[ROWS-1-r][COLS-1-c],
            )
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
