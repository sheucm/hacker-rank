#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
from collections import Counter, defaultdict
def isValid(s):
    if len(s) == 1:
        return "YES"
        
    counter = Counter(s)
    m = defaultdict(int)
    maxCnt = 0
    for ch, cnt in counter.items():
        m[cnt] += 1
        maxCnt = max(maxCnt, cnt)
    
    # All have the same count
    if len(m) == 1:
        return "YES"
    
    # All have the same count, except 1 char have 1 count
    if 1 in m and m[1] == 1 and len(m) - 1 == 1:
        return "YES"
    
    if len(m) == 2 and m[maxCnt-1] > 0 and m[maxCnt] == 1:
        return "YES"
    
    return "NO"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)
    print(result)

    fptr.write(result + '\n')

    fptr.close()
