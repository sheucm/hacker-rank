#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter, defaultdict

MOD = 10**9 + 7
fact = defaultdict(int)
fact[0] = 1
global_count = defaultdict(lambda: Counter())

def initialize(s):
    # This function is called once before all queries.
    for i in range(len(s)):
        fact[i+1] = (fact[i] * (i+1)) % MOD
        global_count[i] = global_count[i-1] + Counter(s[i])

def power(x, n, m):
    if n == 1:
        return x % m
    elif n % 2 == 0:
        return power(x ** 2 % m, n // 2, m)
    else:
        return (x * power(x ** 2 % m, (n - 1) // 2, m)) % m
    
def devision(a, b):
    """For big integer division
    Args:
        a (int): divisor
        b (int): dividend
    Returns:
        int: Quotient
    """
    return (a * power(b, MOD-2, MOD)) % MOD

def answerQuery(s, l, r):
    l, r = l-1, r-1 # Correct to right index in array
    counter = global_count[r] - global_count[l-1]
    single_cnt, pair_cnt, duplicated_cnt = 0, 0, 1
    for ch, cnt in counter.items():
        ch_pair_cnt = cnt // 2
        single_cnt = single_cnt + (cnt % 2)
        pair_cnt = pair_cnt + ch_pair_cnt
        duplicated_cnt = (duplicated_cnt * fact[ch_pair_cnt]) % MOD
    
    ans = fact[pair_cnt] ### Total Combinations (Assume every pair are different)
    ans = devision(ans, duplicated_cnt)  ### Exclude duplicates
    ans = (max(1, single_cnt) * ans) % MOD  ### Add Single Character into the middle of palindrome
    print(ans)
    return ans
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    initialize(s)

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        l = int(first_multiple_input[0])

        r = int(first_multiple_input[1])

        result = answerQuery(s, l, r)

        fptr.write(str(result) + '\n')

    fptr.close()
