#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'journeyToMoon' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY astronaut
#


def journeyToMoon(n, astronaut):
    
    # Write your code here
    graph = [set() for _ in range(n)]
    for p1, p2 in astronaut:
        graph[p1].add(p2)
        graph[p2].add(p1)
        
        
    vis = [False] * n
    
    group_cnts = []
    for p in range(n):
        if vis[p]:
            continue
            
        group_cnts.append(1)
        
        vis[p] = True
        
        
        #### DFS (Will have 1 case of "RecursionError: maximum recursion depth exceeded")####
        # def dfs(_p):
        #     for ch in graph[_p]:
        #         if vis[ch]:
        #             continue
        #         vis[ch] = True
        #         group_cnts[-1] += 1
        #         dfs(ch)
        # dfs(p)
        #### DFS END ####
        
        
        
        #### BFS (Pass) ####
        q = [p]
        while q:
            pop_p = q.pop(0)
            for ch in graph[pop_p]:
                if vis[ch]:
                    continue  
                vis[ch] = True
                group_cnts[-1] += 1
                q.append(ch)
        #### BFS END ####
    

    
    ################ Use this, will cause Timeout ###########
    # ans = 0
    # for i in range(len(group_cnts)):
    #     for j in range(i+1, len(group_cnts)):
    #         ans += group_cnts[i] * group_cnts[j]
    #########################################################
    
    # print(group_cnts)
    ans = 0
    _sum = group_cnts[0]
    for i in range(1, len(group_cnts)):
        ans += _sum * group_cnts[i]
        _sum += group_cnts[i]
        
    print(ans)
    return ans

    
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    p = int(first_multiple_input[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()
