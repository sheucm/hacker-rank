#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#

def highestValuePalindrome(s, n, k):
    # Write your code here
    # if n == 1:
    #     if k >= 1:
    #         return '9'
    #     else:
    #         return s
    
    s = list(s) 
    modified = defaultdict(bool)
    
    ### Make Palindrome
    l, r = 0, n-1
    while l < r:
        if s[l] != s[r]:
            if s[l] >= s[r]:
                s[r] = s[l]
                modified[r] = True
            else:
                s[l] = s[r]
                modified[l] = True
            k -= 1
            if k < 0: return "-1"
        l += 1
        r -= 1
    
    ### Make Max Value
    l, r = 0, n-1
    while l <= r:
        if l == r and k > 0:
            s[l] = '9'
            break
        
        if not modified[l] and not modified[r] and s[l] != '9' and k >= 2:
            s[l] = s[r] = '9'
            k -= 2
        elif (modified[l] or modified[r]) and s[l] != '9' and k >= 1:
            s[l] = s[r] = '9'
            k -= 1
        l += 1
        r -= 1
    
    return "".join(s)
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
