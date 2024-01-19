#!/bin/python3

import os
import sys

#
# Complete the rustMurdered function below.
#

import heapq
def rustMurdered(N, E, roads, S):
    #
    # Write your code here.
    #
    
    graph = [set() for _ in range(N+1)]
    for v1, v2 in roads:
        graph[v1].add(v2)
        graph[v2].add(v1)
    
    
    # All distance should be 1 except for the neighbors of S
    dis = [1] * (N+1)
    dis[S] = 0
    for v in graph[S]:
        dis[v] = -1
        
    
    not_visited = graph[S]
    curr_dis = 2
    
    while not_visited:
        visited = set()
        for v in not_visited:
            diff = not_visited | graph[v]
            if len(diff) < N:
                dis[v] = curr_dis
                visited.add(v)
                
        not_visited -= visited
        curr_dis += 1
    
    
    del dis[S]
    del dis[0]
        
    print(dis)
    return dis 
            
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        roads = []

        for _ in range(m):
            roads.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = rustMurdered(n, m, roads, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
