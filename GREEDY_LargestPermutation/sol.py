#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestPermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def largestPermutation(N, k, arr):
    # Write your code here
    index = {}
    for idx, num in enumerate(arr):
        index[num] = idx
    
    i = 0
    while i < N:
        
        if arr[i] != (N-i) and k > 0:
            # swap
            before_num = arr[i]
            after_num = (N-i)
            
            swap_idx = index[after_num]
            
            arr[i] = after_num
            arr[swap_idx] = before_num
            
            index[before_num] = swap_idx
            index[after_num] = i
            
            k -= 1
        i += 1
    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(n, k, arr)
    print(result)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
