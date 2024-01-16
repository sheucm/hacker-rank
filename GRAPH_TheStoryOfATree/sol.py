#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'storyOfATree' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER k
#  4. 2D_INTEGER_ARRAY guesses
#

from fractions import Fraction

base = 0

def dfs(v, point, vis, graph, guess_map, dp):
    global base
    
    vis[v] = True
    dp[v] = point
    
    for ch in graph[v]:
        if vis[ch]:
            continue
        
        positive = v in guess_map and ch in guess_map[v]
        negative = ch in guess_map and v in guess_map[ch]
        
        if positive and negative:
            base += 1
            dfs(ch, point, vis, graph, guess_map, dp)
        elif positive:
            base += 1
            dfs(ch, point - 1, vis, graph, guess_map, dp)
        elif negative:
            dfs(ch, point + 1, vis, graph, guess_map, dp)
        else:
            dfs(ch, point, vis, graph, guess_map, dp)
        
        

def storyOfATree(n, edges, k, guesses):
    # Write your code here
    # print(n)
    # print(edges)
    # print(k)
    # print(guesses)
    
    # 4
    # [[1, 2], [1, 3], [3, 4]]
    # 2
    # [[1, 2], [3, 4]]
    global base
    
    guess_map = {}
    for p, c in guesses:
        guess_map[p] = guess_map.get(p, []) + [c]
    
    
    graph = [set() for _ in range(n+1)]
    for v1, v2 in edges:
        graph[v1].add(v2)
        graph[v2].add(v1)
    
    
    dp = [0] * (n+1)
    vis = [False] * (n+1)
    
    root = 1
    base = 0
    dfs(root, 0, vis, graph, guess_map, dp)
    
    count = 0
    for i in range(1, n+1):
        if base + dp[i] >= k:
            count += 1
            
    
    ans = ""
    if count == 0:
        ans = "0/1"
    elif count == n:
        ans = "1/1"
    else:
        ans = str(Fraction(count, n))
        
    
    print(ans)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        edges = []

        for _ in range(n - 1):
            edges.append(list(map(int, input().rstrip().split())))

        first_multiple_input = input().rstrip().split()

        g = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        guesses = []

        for _ in range(g):
            guesses.append(list(map(int, input().rstrip().split())))

        result = storyOfATree(n, edges, k, guesses)

        fptr.write(result + '\n')

    fptr.close()
