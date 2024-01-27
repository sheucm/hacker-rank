#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
from collections import defaultdict, Counter
def sherlockAndAnagrams(s):
    # Write your code here
    
    counts = defaultdict(lambda: Counter())
    for i in range(len(s)-1, -1, -1):
        counts[i] = counts[i+1] + Counter(s[i])
    
    counts_2d = defaultdict(lambda: defaultdict(lambda: Counter()))
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            counts_2d[i][j] = counts[i] - counts[j]
    
    ans = 0
    for i in range(len(s)-2, -1, -1):
        for _len in range(1, len(s[i:])):
            l = i+1
            r = l + _len
            while r <= len(s):
                target_cnt = counts_2d[i][i+_len]
                compared_cnt = counts_2d[l][r]
                if target_cnt == compared_cnt:
                    ans += 1
                l += 1
                r += 1
        
    print(ans)
    return ans
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
