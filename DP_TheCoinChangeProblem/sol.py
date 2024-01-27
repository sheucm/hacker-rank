#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#

def getWays(n, coins):
    coins.sort()
    DP = [[0] * (n + 1) for _ in range(len(coins)+1)]
    for r in range(len(coins)+1):
        DP[r][-1] = 1
    for r in range(len(coins)-1, -1, -1):
        for c in range(n-1, -1, -1):
            coin = coins[r]
            DP[r][c] = (
                0 if c+coin >= (n+1) else DP[r][c+coin]
                + DP[r+1][c]
            )
    return DP[0][0]
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)
    print(ways)

    fptr.write(str(ways) + '\n')

    fptr.close()
