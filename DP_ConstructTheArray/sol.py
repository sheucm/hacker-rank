#!/bin/python3

import math
import os
import random
import re
import sys
MOD = 10**9+7

#
# Complete the 'countArray' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER x
#

def countArray(n, k, e, s=1):
    
    ### idx: Decision Tree Level (start from level 1)
    ### val: Node Count
    DP_have_x = [0] * (n+1)
    DP_no_x = [0] * (n+1)
    
    DP_have_x[1] = 0 if x != 1 else 1
    DP_no_x[1] = 1 if x != 1 else 0
    
    for i in range(2, n+1):
        DP_have_x[i] = DP_no_x[i-1]
        DP_no_x[i] = (
            DP_have_x[i-1] * (k - 1) +
            DP_no_x[i-1] * (k - 2)
        ) % MOD
    return DP_have_x[n]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = int(first_multiple_input[2])

    answer = countArray(n, k, x)

    fptr.write(str(answer) + '\n')

    fptr.close()
