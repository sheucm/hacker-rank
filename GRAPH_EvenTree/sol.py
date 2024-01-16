#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the evenForest function below.
def evenForest(N, t_edges, t_from, t_to):
    
    # Build grpah
    graph = [set() for _ in range(N+1)]
    for i in range(t_edges):
        graph[t_from[i]].add(t_to[i])
        graph[t_to[i]].add(t_from[i])
    
    ans = 0
    vis = [False] * (N+1)
    def dfs(_v):
        nonlocal ans
        total_ch_cnt = 0
        for ch in graph[_v]:
            if vis[ch]:
                continue
            vis[ch] = True
            ch_cnt = dfs(ch)
            if ch_cnt % 2 == 0:
                ans += 1
            total_ch_cnt += ch_cnt
        
        return total_ch_cnt + 1
                
    vis[1] = True
    dfs(1)
    print(ans)
    return ans 

    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t_nodes, t_edges = map(int, input().rstrip().split())

    t_from = [0] * t_edges
    t_to = [0] * t_edges

    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())

    res = evenForest(t_nodes, t_edges, t_from, t_to)

    fptr.write(str(res) + '\n')

    fptr.close()
