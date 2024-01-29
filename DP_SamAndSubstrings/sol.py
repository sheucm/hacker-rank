#!/bin/python3

import math
import os
import random
import re
import sys

MOD = 10**9 + 7

#
# Complete the 'substrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING n as parameter.
#
def substrings(n):
    ### Represent the sum of all combination with n[i] within n[:i+1] 
    ### For example:  n = "123", then DP1[2] (index=2) = 3 + 23 + 123 = 149
    ### 3 + 23 + 123 = (12 + 2) + 3 * 3 = DP1[1] + n[2] * (2+1) = DP1[i-1] + n[i] * (i + 1)
    DP1 = [0] * len(n)
    DP1[0] = int(n[0])
    
    ### Represent the sum of all combination within n[:i+1] 
    ### For example:  n = "123", then DP2[2] (index=2) = 1 + 2 + 3 + 12 + 23 + 123 = 164
    ### 1 + 2 + 3 + 12 + 23 + 123 = (3 + 23 + 123) + (1 + 2 + 12) = DP1[2] + DP2[1] = DP1[i] + DP2[i-1]
    DP2 = [0] * len(n)
    DP2[0] = int(n[0])
    
    for i in range(1, len(n)):
        DP1[i] = (DP1[i-1] * 10 + int(n[i]) * (i+1)) % MOD
        DP2[i] = (DP1[i] + DP2[i-1]) % MOD
    return DP2[len(n)-1]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = input()

    result = substrings(n)
    print(result)
    
    fptr.write(str(result) + '\n')

    fptr.close()
