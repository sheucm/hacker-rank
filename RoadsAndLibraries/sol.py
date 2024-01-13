#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#

def roadsAndLibraries(n, c_lib, c_road, cities):
    # Write your code here
    
    
    # BFS
    graph = [set() for _ in range(n+1)]
    for v1, v2 in cities:
        graph[v1].add(v2)
        graph[v2].add(v1)
    
    
    vis = [False] * (n+1)
    
    
    lib_cnt = 0
    road_cnt = 0
    for v in range(1, n+1):
        
        if vis[v]:
            continue
        
        lib_cnt += 1
        
        vis[v] = True
        q = [v]
        
        while q:
            pop_v = q.pop(0)
            for ch in graph[pop_v]:
                if vis[ch]:
                    continue
                
                vis[ch] = True
                road_cnt += 1
                q.append(ch)
    
    cost = lib_cnt * c_lib + road_cnt * c_road
    
    cost2 = n * c_lib
    
    return min(cost, cost2)
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
