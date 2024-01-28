#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'redJohn' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
import math
def get_ways(n):
    if n <= 3:
        return 1
    if n == 4:
        return 2
    return get_ways(n-1) + get_ways(n-4)

def sieve_prime(n):
    primes = [True] * (n+1)
    primes[0], primes[1] = False, False
    for i in range(2, int(math.sqrt(n))+1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    return sum([1 for is_p in primes if is_p])

def redJohn(n):
    ways = get_ways(n)
    prime_count = sieve_prime(ways)
    return prime_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = redJohn(n)

        fptr.write(str(result) + '\n')

    fptr.close()
