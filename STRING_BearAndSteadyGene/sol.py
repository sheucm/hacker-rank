#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'steadyGene' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING gene as parameter.
#
from collections import Counter, defaultdict
def steadyGene(gene):
    
    counter = Counter(gene)
    STEADY = len(gene) // 4
    
    def is_valid():
        return (
            counter['A'] <= STEADY and
            counter['C'] <= STEADY and
            counter['T'] <= STEADY and
            counter['G'] <= STEADY
        )
    if is_valid(): return 0
    
    ans = float('inf')
    l, r = 0, 0 # the range that need to be modified
    while l <= r and r < len(gene):
        counter[gene[r]] -= 1
        r += 1
        
        while is_valid() and l <= r:
            ans = min(ans, (r - l))
            counter[gene[l]] += 1
            l += 1
        
    return ans
    
            
        
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    gene = input()

    result = steadyGene(gene)

    fptr.write(str(result) + '\n')

    fptr.close()
