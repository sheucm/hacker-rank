
# Category
# 1. BFS / DFS 
    # - DFS: remember to set below settings to avoid "RecursionError: maximum recursion depth exceeded"
    # '''
    # import sys
    # sys.setrecursionlimit(100000)
    # '''
# 2. Shortest Path (Dijkstra Algorithm)
#     - BFS
# 3. MST (Minimum Spanning Tree) (Prim's Algorithm)
#     - BFS
#     - kruskal algo
# 4. clique
# 5. crab (undirected graph)
    # - Ford-Fulkerson Algorithm  (Max Flow Alg.)
# 6. Circular tour problem. https://www.hackerrank.com/challenges/truck-tour/problem


# -------------------------------------------------------------------------------------

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

######### Ford Fulkerson algorithm (Max Flow Algorithm) ######### 
# Reference: https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/
class Graph:
 
    def __init__(self, graph):
        self.graph = graph  # residual graph
        self. ROW = len(graph)
        # self.COL = len(gr[0])
 
    '''Returns true if there is a path from source 's' to sink 't' in
    residual graph. Also fills parent[] to store the path '''
 
    def BFS(self, s, t, parent):
 
        # Mark all the vertices as not visited
        visited = [False]*(self.ROW)
 
        # Create a queue for BFS
        queue = []
 
        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True
 
         # Standard BFS Loop
        while queue:
 
            # Dequeue a vertex from queue and print it
            u = queue.pop(0)
 
            # Get all adjacent vertices of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                      # If we find a connection to the sink node, 
                    # then there is no point in BFS anymore
                    # We just have to set its parent and can return true
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True
 
        # We didn't reach sink in BFS starting 
        # from source, so return false
        return False
             
     
    # Returns the maximum flow from s to t in the given graph
    def FordFulkerson(self, source, sink):
 
        # This array is filled by BFS and to store path
        parent = [-1]*(self.ROW)
 
        max_flow = 0 # There is no flow initially
 
        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent) :
 
            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while(s !=  source):
                path_flow = min (path_flow, self.graph[parent[s]][s])
                s = parent[s]
 
            # Add path flow to overall flow
            max_flow +=  path_flow
 
            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while(v !=  source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
 
        return max_flow
 
  
# Create a graph given in the above diagram
 
graph = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]
 
g = Graph(graph)
 
source = 0; sink = 5
  
print ("The maximum possible flow is %d " % g.FordFulkerson(source, sink))
 
# This code is contributed by Neelam Yadav














# -------------------------------------------------------------------------------------
# Kruskal's algorithm (Build MST: Minimum Spanning Tree)
# Reference: https://www.youtube.com/watch?v=71UQH7Pr9kU
N = 5
E = 6
edges = [  # Format: v1, v2, weight
    [1, 3, 5],
    [4, 5, 0],
    [2, 1, 3],
    [3, 2, 1],
    [4, 3, 4],
    [4, 2, 2],
]

parent = [i for i in range(N+1)]

def find(i):
	while i != parent[parent[i]]:
		parent[i] = parent[parent[i]]
		i = parent[i]
	return i 

def union(x, y):
    p_x = find(x)
    p_y = find(y)
    parent[p_y] = p_x

def is_connect(x, y):
    p_x = find(x)
    p_y = find(y)
    return p_x == p_y


mst = [set() for _ in range(N+1)]

edges = sorted(edges, key=lambda x: x[2])
for v1, v2, w in edges:
    if not is_connect(v1, v2):
        union(v1, v2)
        mst[v1].add((v2, w))
        mst[v2].add((v1, w))

print(mst)