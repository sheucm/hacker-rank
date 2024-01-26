#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#

def bfs(n, m, edges, s):
    m = {}
    
    graph = [set() for _ in range(n+1)]
    for v1, v2 in edges:
        graph[v1].add(v2)
        graph[v2].add(v1)
    
    def bfs(v):
        vis = [False] * (n+1)
        q = [(v, 0)]
        while q:
            v, step = q.pop(0)
            if not v:
                continue
            if vis[v]:
                continue
            vis[v] = True
            m[v] = step
            for u in graph[v]:
                q.append((u, step+1))
    bfs(s)
    ans = []
    for i in range(1, n+1):
        if i == s:
            continue
        if i not in m:
            ans.append(-1)
        else:
            ans.append(m[i] * 6)
    return ans
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
