#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'mandragora' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY H as parameter.
#

def mandragora(H):
    
    ### Tranform Story Problem to Code Problem
    ### Point = (START_POINT + eat_count) * sum(not_eat_healths)
    ### Return Max(Points)
    
    ### Solution: Greedy + DP
    
    START = 1
    H.sort()
    
    DP = [0] * len(H) # H Sum from H[i] to H[-1]
    DP[-1] = H[-1]
    for i in range(len(H)-2, -1, -1):
        DP[i] = DP[i+1] + H[i]
    
    max_point = 0
    for i in range(len(H)):
        point = (START + i) * DP[i]
        max_point = max(max_point, point)
    return max_point
        
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        H = list(map(int, input().rstrip().split()))

        result = mandragora(H)

        fptr.write(str(result) + '\n')

    fptr.close()
