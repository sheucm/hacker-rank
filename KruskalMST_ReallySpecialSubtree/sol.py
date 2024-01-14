#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kruskals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#

import heapq

def kruskals(N, g_from, g_to, g_weight):
    # Write your code here
    
    _min_w = float('inf')
    start = -1
    
    graph = [set() for _ in range(N+1)]
    for i, w in enumerate(g_weight):
        v1 = g_from[i]
        v2 = g_to[i]
        graph[v1].add((v2, w))
        graph[v2].add((v1, w))
        
        if w < _min_w:
            _min_w = w
            start = v1
    
    vis = [False] * (N+1)
    
    q = [(0, start)]  # w, v
    
    ans = 0
    n_left = N
    
    while q and n_left > 0:
        w, v = heapq.heappop(q)
        if vis[v]:
            continue
        vis[v] = True
        ans += w
        n_left -= 1
        
        for ch, ch_w in graph[v]:
            if vis[ch]:
                continue
            heapq.heappush(q, (ch_w, ch))
            
    print(ans)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    res = kruskals(g_nodes, g_from, g_to, g_weight)

    # Write your code here.
    fptr.write(str(res) + '\n')

    fptr.close()
