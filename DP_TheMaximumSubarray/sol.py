#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    # Write your code here
    ### Problem: Maximum Subarray + Similar LIS (Longest Increasing Subsequence)
    
    # Calculate Max Subarray
    DP1 = [0] * len(arr)
    DP1[0] = arr[0]
    for i in range(1, len(arr)):
        DP1[i] = max(
            arr[i],
            arr[i] + DP1[i-1]
        )
    max_substr = max(DP1)
    
    # Calculate Max Sequence
    DP2 = [0] * len(arr)
    DP2[0] = arr[0]
    maxIdx = 0
    maxVal = arr[0]
    for i in range(1, len(arr)):
        DP2[i] = max(
            arr[i],
            arr[i] + DP2[maxIdx]
        )
        if DP2[i] > maxVal:
            maxVal = DP2[i]
            maxIdx = i
    max_seq = max(DP2)
    return [max_substr, max_seq]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)
        print(result)
        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
