
import math
import os
import random
import re
import sys
from collections import defaultdict
import heapq

# Complete the 'shop' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. STRING_ARRAY centers
#  4. 2D_INTEGER_ARRAY roads
#

def shop(n, k, centers, roads):
    
    # Build Bit Masking
    init_fishset_m = defaultdict(int)
    for v, center_str in enumerate(centers):
        tokens = center_str.split(' ')
        for fish_type in tokens[1:]:
            init_fishset_m[v+1] |= 1 << (int(fish_type) - 1)

    
    # Build Graph
    graph = [set() for _ in range(n+1)]
    for v1, v2, w in roads:
        graph[v1].add((v2, w))
        graph[v2].add((v1, w))
    
    
    # Build DP array
    vis = [ [False] * (2 ** k) for _ in range(n+1)]
    dis = [ [float('inf')] * (2 ** k) for _ in range(n+1)]
    
    vis[1][init_fishset_m[1]] = True
    dis[1][init_fishset_m[1]] = 0
    
    
    # BFS
    q = [(0, 1, init_fishset_m[1])]   # distance, vertex, fishset
    heapq.heapify(q)
    while q:
        d, v, fishset = heapq.heappop(q)
        for ch, w in graph[v]:
            
            new_fishset = fishset | init_fishset_m[ch]
            new_d = d + w
            
            if vis[ch][new_fishset] and dis[ch][new_fishset] <= new_d:
                continue
            
            vis[ch][new_fishset] = True
            dis[ch][new_fishset] = new_d
            
            heapq.heappush(q, (new_d, ch, new_fishset))
        
    
    
    # Get Answer from DP 2D array
    ans = dis[n][2 ** k - 1]
    for i in range(2 ** k - 2, 0, -1):
        if dis[n][i] == float('inf'):
            continue
        for j in range(0, i):
            if dis[n][j] == float('inf'):
                continue
            
            sum_fishset = i | j
            sum_d = max(dis[n][i], dis[n][j])
            
            if sum_fishset == 2 ** k - 1 and sum_d < ans:
                ans = sum_d
    print(ans)
    return ans
            
            
    
    

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    centers = []

    for _ in range(n):
        centers_item = input()
        centers.append(centers_item)

    roads = []

    for _ in range(m):
        roads.append(list(map(int, input().rstrip().split())))

    res = shop(n, k, centers, roads)

    fptr.write(str(res) + '\n')

    fptr.close()