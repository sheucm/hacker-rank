#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'unboundedKnapsack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def unboundedKnapsack(k, arr):
    DP = [False] * (k+1)
    DP[0] = True
    arr = list(set(arr))
    for i in range(1, k+1):
        val = False
        for n in arr:
            if i - n >= 0:
                val = val or DP[i-n]
        DP[i] = val
    
    for i in range(k, 0, -1):
        if DP[i]:
            return i
    return 0
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for _ in range(t):
        
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        arr = list(map(int, input().rstrip().split()))

        result = unboundedKnapsack(k, arr)

        fptr.write(str(result) + '\n')

    fptr.close()
