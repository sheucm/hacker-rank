# N: number of nodes
# edges: List of edge(v1, v2)
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