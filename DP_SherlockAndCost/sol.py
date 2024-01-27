#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cost' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY B as parameter.
#

def cost(B):
    # Write your code here
    
    pre1 = 0 # For max value of choosing largest value
    pre2 = 0 # For max value of choosing 1
    max1 = 0
    max2 = 0
    
    for i in range(1, len(B)):
        # Pick B[i] (largest value)
        max1 = max(abs(B[i] - B[i-1]) + pre1, abs(B[i] - 1) + pre2)
        
        # Pick 1 (lowest value)
        max2 = abs(1 - B[i-1]) + pre1
        
        pre1 = max1
        pre2 = max2
    
    return max(max1, max2)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        B = list(map(int, input().rstrip().split()))

        result = cost(B)

        fptr.write(str(result) + '\n')

    fptr.close()
