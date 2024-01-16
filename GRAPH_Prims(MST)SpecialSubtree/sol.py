#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'prims' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER start
#

import heapq

def prims(n, edges, start):
    """prims

    Args:
        n (int): number of nodes
        edges (List[List[int]]): edge list
        start (int): start node

    Returns:
        int: min sum of edge weight
    """
    
    graph = [set() for _ in range(n+1)]
    for v1, v2, w in edges:
        graph[v1].add((v2, w))
        graph[v2].add((v1, w))
    
    vis = [False] * (n+1)
    q = [(0, start)]  # w, v
    
    
    _sum = 0
    while q:
        w, v = heapq.heappop(q)
        if vis[v]:
            continue
        vis[v] = True
        _sum += w
        for ch_v, ch_w in graph[v]:
            heapq.heappush(q, (ch_w, ch_v))
    print(_sum)
    return _sum
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    start = int(input().strip())

    result = prims(n, edges, start)

    fptr.write(str(result) + '\n')

    fptr.close()
