#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickestWayUp' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY ladders
#  2. 2D_INTEGER_ARRAY snakes
#
from collections import defaultdict

def getRollCount(snake_m, start, end):
    curr = start
    cnt = 0
    while curr < end:
        die = 6
        while curr + die in snake_m:
            die -= 1
            if die == 0:
                raise Exception('no step to go')
       
        curr += die
        cnt += 1
    return cnt

def quickestWayUp(ladders, snakes):
    # Write your code here
    #return int : min moves
    
    # print(ladders)
    # print(snakes)
    # [[32, 62], [42, 68], [12, 98]]
    # [[95, 13], [97, 25], [93, 37], [79, 27], [75, 19], [49, 47], [67, 17]]
    
    graph = {}  # Directed Graph
    for v1, v2 in (ladders + snakes):
        graph[v1] = v2
    
    vis = [False] * 101
    
    q = [(1, 0)]
    vis[1] = True
    ans = -1
    while q:
        v, rolls = q.pop(0)
        if v == 100:
            ans = rolls
            break
        
        for i in range(1, 7):
            next_v = v + i
            if next_v > 100:
                continue
                
            if vis[next_v]:
                continue
            
            if next_v in graph:
                next_v = graph[next_v]
            
            vis[next_v] = True
            q.append((next_v, rolls+1))
            
    
    print(ans)
    return ans
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        ladders = []

        for _ in range(n):
            ladders.append(list(map(int, input().rstrip().split())))

        m = int(input().strip())

        snakes = []

        for _ in range(m):
            snakes.append(list(map(int, input().rstrip().split())))

        result = quickestWayUp(ladders, snakes)

        fptr.write(str(result) + '\n')

    fptr.close()
