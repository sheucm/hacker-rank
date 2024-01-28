#!/bin/python3

import math
import os
import random
import re
import sys
sys.setrecursionlimit(100000000)
#
# Complete the 'abbreviation' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#
from collections import defaultdict
cache = {}
def abbreviation(a, b):
    
    ### Similar LCS problem. (Longest Common Subsequence)
    
    DP = [[False] * (len(a)+1) for _ in range(len(b)+1)]
    
    ## init DP
    DP[-1][-1] = True
    for r in range(len(b)):
        DP[r][-1] = False
    for c in range(len(a)-1, -1, -1):
        DP[-1][c] = False if a[c].isupper() else DP[-1][c+1]
    
    ## cal DP
    for r in range(len(b)-1, -1, -1):
        for c in range(len(a)-1, -1, -1):
            if a[c].isupper():
                DP[r][c] = (a[c] == b[r]) and DP[r+1][c+1]
            else:
                DP[r][c] = DP[r][c+1] or (
                    DP[r+1][c+1] if a[c].upper() == b[r] else False
                )
    return DP[0][0]
        
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)
        result = "YES" if result else "NO"
        print(result)

        fptr.write(result + '\n')

    fptr.close()
