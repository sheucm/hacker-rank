#!/bin/python3

import math
import os
import random
import re
import sys
MOD = 10**9+7
def power(x, y):
    if y == 1:
        return x
    if y % 2 == 0:
        return power(x**2 % MOD, y//2)
    else:
        return x * power(x**2 % MOD, y//2)
#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#
def legoBlocks(n, m):
    # Write your code here
    DP_R = [0] * (m+1) # The DP of row combination
    DP_T = [0] * (m+1) # The DP of total combination (include unsolid (bad) and solid)
    DP_S = [0] * (m+1) # The DP of solid combination (total - unsolid)
    
    ### Init DP
    DP_T[0], DP_S[0] = 1, 1
    DP_T[1], DP_S[1] = 1, 1
    
    ### Calculate DP_R
    for i in range(1, m+1):
        if i <= 4:
            DP_R[i] = 2 ** (i-1)
        else:
            DP_R[i] = (DP_R[i-1] + DP_R[i-2] + DP_R[i-3] + DP_R[i-4]) % MOD
    
    ### Calculate DP_T / DP_S
    for i in range(2, m+1):
        # Notice: Cannot use DP_R[i] ** n, otherwise overflow
        DP_T[i] = power(DP_R[i], n) % MOD
        
        # Notice: Cannot use sum(), otherwise overflow
        unsolid = 0
        for j in range(1, i):
            unsolid = (unsolid + DP_S[j] * DP_T[i-j]) % MOD
        
        DP_S[i] = (DP_T[i] - unsolid) % MOD
    return DP_S[m] % MOD
        
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
