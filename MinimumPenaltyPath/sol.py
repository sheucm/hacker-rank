#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulPath' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY edges
#  2. INTEGER A
#  3. INTEGER B
#
import heapq
def beautifulPath(n, edges, start, end):
    # Write your code here
    # int beautifulPath(vector<vector<int>> edges, int A, int B) 
    
    
    graph = [set() for _ in range(n+1)]
    for v1, v2, w in edges:
        graph[v1].add((v2, w))
        graph[v2].add((v1, w))
    
    
    
    cost = [set() for j in range(n+1)]
    q = [(0, start)]
    
    while q:
        w, v = heapq.heappop(q)
        for ch, ch_w in graph[v]:
            new_w = ch_w | w
            
            if new_w not in cost[ch] and new_w <= 1024:
                cost[ch].add(new_w)
                heapq.heappush(q, (new_w, ch))
    
    ans = sorted(cost[end])[0] if cost[end] else -1
    
    print(ans)
    return ans
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    second_multiple_input = input().rstrip().split()

    A = int(second_multiple_input[0])

    B = int(second_multiple_input[1])

    result = beautifulPath(n, edges, A, B)

    fptr.write(str(result) + '\n')

    fptr.close()
