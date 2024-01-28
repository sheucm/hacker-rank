#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'longestCommonSubsequence' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def longestCommonSubsequence(a, b):
    ### Same question as Leetcode 1143. Longest Common Subsequence
    
    DP_cnt = [[0] * (len(b)+1) for _ in range(len(a)+1)]
    DP_seq = [[set() for _1 in range((len(b)+1))] for _2 in range(len(a)+1)]
    
    
    for r in range(len(a)-1, -1, -1):
        for c in range(len(b)-1, -1, -1):
            if a[r] == b[c]:
                DP_cnt[r][c] = 1 + DP_cnt[r+1][c+1]
                
                if DP_seq[r+1][c+1]:
                    for seq_tuple in DP_seq[r+1][c+1]:
                        seq_list = [a[r]] + list(seq_tuple)
                        DP_seq[r][c].add(tuple(seq_list))
                else:
                    DP_seq[r][c].add((a[r],))
                
            else:
                if DP_cnt[r][c+1] > DP_cnt[r+1][c]:
                    DP_cnt[r][c] = DP_cnt[r][c+1]
                    DP_seq[r][c] = DP_seq[r][c+1]
                elif DP_cnt[r][c+1] < DP_cnt[r+1][c]:
                    DP_cnt[r][c] = DP_cnt[r+1][c]
                    DP_seq[r][c] = DP_seq[r+1][c]
                else:
                    DP_cnt[r][c] = DP_cnt[r+1][c]
                    DP_seq[r][c] = DP_seq[r][c+1] | DP_seq[r+1][c]
    
    ans_list = [list(tup) for tup in DP_seq[0][0]]
    return ans_list[0]
                
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = longestCommonSubsequence(a, b)
    print(result)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
