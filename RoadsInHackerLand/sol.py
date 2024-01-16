#!/bin/python3
import os
#
# Complete the 'roadsInHackerland' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY roads
#
from collections import defaultdict

def roadsInHackerland(n, edges):
    # Write your code here
    
    parent = [i for i in range(n+1)]
    
    def find(x):
        while x != parent[parent[x]]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(x, y):
        p_x = find(x)
        p_y = find(y)
        parent[p_y] = p_x
    
    def is_connect(x, y):
        p_x = find(x)
        p_y = find(y)
        return p_x == p_y
    
    
    # Create MST Tree
    tree = [set() for _ in range(n+1)]  # MST
    
    edges = sorted(edges, key=lambda x: x[2])
    for v1, v2, w in edges:
        if not is_connect(v1, v2):
            union(v1, v2)
            tree[v1].add((v2, w))
            tree[v2].add((v1, w))
    
    # Calculate each edge count
    edge_cnt = [0] * len(edges)
    def dfs(v, par = -1):
        total = 1
        
        for ch, ch_w in tree[v]:
            if ch == par:
                continue
            child_total = dfs(ch, v)
            
            edge_cnt[ch_w] = child_total * (n - child_total)
            
            total += child_total
        return total
            
    dfs(1)
    
    ans = 0
    for i, cnt in enumerate(edge_cnt):
        ans += cnt * (1 << i)

    
    ans = str(bin(ans))[2:]
    print(ans)
    return ans
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    roads = []

    for _ in range(m):
        roads.append(list(map(int, input().rstrip().split())))

    result = roadsInHackerland(n, roads)

    fptr.write(result + '\n')

    fptr.close()
