#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def commonChild(s1, s2):
    # Write your code here
    ### Same question with Leetcode (Brind75) 1143. Longest Common Subsequence
    DP = [[0] * (len(s2)+1) for _ in range(len(s1)+1)]
    for i1 in range(len(s1)-1, -1, -1):
        for i2 in range(len(s2)-1, -1, -1):
            if s1[i1] == s2[i2]:
                DP[i1][i2] = 1 + DP[i1+1][i2+1]
            else:
                DP[i1][i2] = max(
                    DP[i1+1][i2],
                    DP[i1][i2+1]
                )
    return DP[0][0]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
