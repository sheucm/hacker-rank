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
#  1. INTEGER n: # of nodes
#  2. INTEGER m: # of edges
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s: start
#
    

def bfs(N, E, edges, start):
    
    # # Return: List[int]
    # # Write your code here
    
    WEIGHT = 6
    
    graph = [set() for _ in range(N+1)]
    for v1,v2 in edges:
        graph[v1].add(v2)
        graph[v2].add(v1)
        
    
    distances = [-1] * (N+1)
    distances[start] = 0
    
    vis = [False] * (N+1)
    vis[start] = True
    
    q = [(start, 0)]
    while q:
        pop_v, dis = q.pop(0)
        
        for ch in graph[pop_v]:
            if vis[ch]:
                continue
                
            vis[ch] = True
            distances[ch] = dis + WEIGHT
            q.append((ch, dis + WEIGHT))
        
    ans = []
    for idx, d in enumerate(distances):
        if idx == 0:
            continue
        if d == 0:
            continue
        ans.append(d)
    
    print(ans)
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

