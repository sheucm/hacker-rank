#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bricksGame' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def bricksGame(arr):
    
    ### Solution: DP(Bottom-up) + Greedy
    DP = [0] * len(arr)
    
    total = 0
    for i in range(len(arr)-1, -1, -1):
        total += arr[i]
        if i >= len(arr) - 3:
            DP[i] = total
        else:
            DP[i] = max(
                total - DP[i+1],
                total - DP[i+2],
                total - DP[i+3]
            )
    return DP[0]
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = bricksGame(arr)
        print(result)

        fptr.write(str(result) + '\n')

    fptr.close()
