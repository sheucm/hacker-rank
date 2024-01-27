

#!/bin/python3

import math
import os
import random
import re
import sys
sys.setrecursionlimit(10000000)
MOD = 10**9+7
#
# Complete the 'kingdomDivision' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY roads
#

def spanningTree(root, graph):
    tree = [set() for _ in range(n+1)]
    post_order = []
    path = set()
    def dfs(v, pa=-1):
        if v in path:
            return
        path.add(v)
        for u in graph[v]:
            if u == pa: continue
            tree[v].add(u)
            dfs(u, v)
        path.remove(v)
        post_order.append(v)
    dfs(root)
    return tree, post_order

def coloring(tree, root, post_order, n):
    DP_true = [0] * (n+1)  # safe variations where `v` and it's parent `p` has the same color
    DP_false = [0] * (n+1) # safe variations where `v` and it's parent `p` has different colors
    for v in post_order:
        if not tree[v]: # leaf node
            DP_true[v] = 1
            DP_false[v] = 0
        else:
            cases, invalid = 1, 1
            for child in tree[v]:
                cases *= DP_true[child] + DP_false[child]
                invalid *= DP_false[child]
            DP_true[v] = cases
            DP_false[v] = cases - invalid
    return DP_false[root] * 2
       

def kingdomDivision(n, roads):
    
    ### 1. Build Graph
    graph = [set() for _ in range(n+1)]
    for v1, v2 in roads:
        graph[v1].add(v2)
        graph[v2].add(v1)
    
    ### 2. Use DFS (post order)  (topo order) to complete DP
    root = 1
    tree, post_order = spanningTree(root, graph)
    ans = coloring(tree, root, post_order, n)
    return ans % MOD
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    roads = []

    for _ in range(n - 1):
        roads.append(list(map(int, input().rstrip().split())))

    result = kingdomDivision(n, roads)
    print(result)

    fptr.write(str(result) + '\n')

    fptr.close()
    
    
    
