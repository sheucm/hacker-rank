#!/bin/python3

import math
import os
import random
import re
import sys
sys.setrecursionlimit(10000000)
sys.set_int_max_str_digits(500000)
#
# Complete the 'fibonacciModified' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER t1
#  2. INTEGER t2
#  3. INTEGER n
#

def fibonacciModified(t1, t2, n):
    
    ### Solution1: DP
    DP = [0] * (n+1)
    DP[1] = t1
    DP[2] = t2
    for i in range(3, n+1):
        DP[i] = DP[i-2] + DP[i-1] ** 2
    return DP[n]
    
    ### Solution2: Recursive
    # if n == 3:
    #     return t1 + t2 ** 2
    # return fibonacciModified(t2, t1 + t2**2, n-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    t1 = int(first_multiple_input[0])

    t2 = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    result = fibonacciModified(t1, t2, n)
    print(result)
    
    fptr.write(str(result) + '\n')

    fptr.close()
