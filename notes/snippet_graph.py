# N: number of nodes
# edges: List of [v1, v2]
# start: Start Node




#### Build Graph ####
graph = [set() for i in range(N)]
for v1, v2 in edges:
    graph[v1].add(v2)
    graph[v2].add(v1)
#### Build Graph END ####


vis = [False] * N
vis[start] = True









#### BFS ####
q = [start]
while q:
    pop_v = q.pop(0)
    for ch in graph[pop_v]:
        if vis[ch]:
            continue
        vis[ch] = True
        # ...
        q.append(ch)
#### BFS END ####








#### DFS ####
def dfs(_v):
    for ch in graph[_v]:
        if vis[ch]:
            continue
        vis[ch] = True
        # ...
        dfs(ch)
dfs(start)
#### DFS END ####









##### How to build a graph with "edge weight" 
# N: number of nodes
# edges: List of [v1, v2, weight]
# start: Start Node

#### Build Graph ####
graph = [set() for _ in range(N)]
for v1, v2, w in edges:
    graph[v1].add((v2, w))
    graph[v2].add((v1, w))
#### Build Graph END ####









# -------------------------------------------------------------------------------------


####### Dijkstra Algorithm - Shortest Path ########
# N: number of nodes
# edges: List of [v1, v2, weight]
# start: Start Node
# graph: (already built)
# start_v: start vertex

# 1. Dijkstra Algorithm   (on weight / un-weight graph)  (no negative weight)
# Skills:
#     - bfs
#     - min heap queue (Greedy)

import heapq

# Build DP
vis = [False] * N
dis = [float('inf')] * N

vis[start_v] = True
dis[start_v] = 0
q = [(0, start_v)]  # accumulated distance, vertex
heapq.heapify(q)    # Min Heap

# BFS
while q:
    d, v = heapq.heappop(q)  # Greedy
    for ch, w in graph[v]:
        new_d = d + w
        if vis[ch] and dis[ch] <= new_d:
            continue
        vis[ch] = True
        dis[ch] = new_d
        heapq.heappush(q,(new_d, ch))
print(dis)
####### END of Dijkstra Algorithm - Shortest Path ########



# -------------------------------------------------------------------------------------