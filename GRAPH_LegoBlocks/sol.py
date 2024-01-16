#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n (height)
#  2. INTEGER m (width)
#

def legoBlocks(H, W):
    R = [0] * (W+1)  # The DP of row combination
    T = [0] * (W+1)  # The DP of total combination (include unsolid (bad) and solid)
    S = [0] * (W+1)  # The DP of solid combination (total - unsolid)
    MOD = 10 ** 9 + 7
    
    
    R[:5] = [0,1,2,4,8]   # Initial values for DP
    
    # Calculate "R"
    for w in range(5, W+1):
        R[w] = (R[w-1] + R[w-2] + R[w-3] + R[w-4]) % MOD
    
    
    # Calculate "T"
    # Note: Here cannot use "T[w] ** H" as will cause number overflow, so use MOD to avoid it.
    for w in range(1, W+1):
        T[w] = 1
        for _ in range(H):
            T[w] = (T[w] * R[w]) % MOD
        
    # Calculate "S"
    S[1] = 1
    for w in range(2, W+1):
        bad = 0
        for i in range(1, w):
            bad = (bad + S[i] * T[w-i]) % MOD
        
        S[w] = (T[w] - bad) % MOD
    

    return S[W] % MOD
    

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


