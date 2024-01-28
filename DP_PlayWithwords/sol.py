#!/bin/python3

import math
import os
import random
import re
import sys
sys.setrecursionlimit(10000000)
#
# Complete the 'playWithWords' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.

def get_max_palindrome_length(s, DP, start, end):
    
    if start > end:
        return 0
    
    if DP[start][end] != -1:
        return DP[start][end]
    
    result = 0
    if s[start] == s[end]:
        length = 2 if start != end else 1
        result = length + get_max_palindrome_length(s, DP, start+1, end-1)
    else:
        result = max(
            get_max_palindrome_length(s, DP, start, end-1),
            get_max_palindrome_length(s, DP, start+1, end),
        )
    DP[start][end] = result
    return result
    

def playWithWords(s):
    
    DP = [[-1] * (len(s)+1) for _ in range(len(s)+1)]
    
    max_product = 0
    for i in range(len(s)):
        product = get_max_palindrome_length(s, DP, 0, i) * get_max_palindrome_length(s, DP, i+1, len(s)-1)
        max_product = max(max_product, product)
    return max_product
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = playWithWords(s)

    fptr.write(str(result) + '\n')

    fptr.close()
