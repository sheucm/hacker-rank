#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getCost' function below.
#
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

def getCost(N, E, g_from, g_to, g_weight):
    """getCost

    Args:
        N (int): number of nodes
        E (int): number of edges
        g_from (List[int]): start node of edge
        g_to (List[int]): end node of edge
        g_weight (List[int]): weight of edge

    Returns:
        string: print "NO PATH EXISTS" if no path else print minimum cost
    """
    
    graph = [set() for _ in range(N+1)]
    for i in range(E):
        graph[g_from[i]].add((g_to[i], g_weight[i]))
        graph[g_to[i]].add((g_from[i], g_weight[i]))
    
    cost = [float('inf')] * (N+1)
    vis = [False] * (N+1)
    vis[1] = True
    cost[1] = 0
    q = [(0, 1)]
    
    
    while q:
        w, v = heapq.heappop(q)
        for ch, ch_w in graph[v]:
            new_cost = w + (ch_w - w if ch_w - w > 0 else 0)
            
            if vis[ch] and cost[ch] <= new_cost:
                continue
            vis[ch] = True
            cost[ch] = new_cost
            heapq.heappush(q, (new_cost, ch))
    
    
    ans = "NO PATH EXISTS" if cost[N] == float('inf') else f"{cost[N]}"
    print(ans)
    return ans
            
            
    
    
    
    

if __name__ == '__main__':
    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    getCost(g_nodes, g_edges, g_from, g_to, g_weight)
