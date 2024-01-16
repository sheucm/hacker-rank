
class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.N = len(graph)   # number of nodes
    
    
    def bfs(self, source, sink, parent):
        
        vis = [False] * self.N
        vis[source] = True
        
        q = [source]
        while q:
            v = q.pop(0)
            for u, w in enumerate(self.graph[v]):
                if vis[u] or self.graph[v][u] <= 0:
                    continue
                vis[u] = True
                parent[u] = v
                q.append(u)
                if u == sink:
                    return True
        
        return False
        
        
        
    def FordFulkerson(self, source, sink):
        
        parent = [-1] * self.N
        
        max_flow = 0
        
        while self.bfs(source, sink, parent):
            
            path_flow = float('inf')
            v = sink
            while v != source:
                path_flow = min(path_flow, self.graph[parent[v]][v])
                v = parent[v]
            
            max_flow += path_flow
            
            
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = u
        
        return max_flow
        


def crabGraphs(N, T, edges):
    """crabGraphs

    Args:
        N (int): number of nodes
        T (int): max of crab feet
        edges (List[int]): list of edge

    Returns:
        int: max vertex of all crabs
    """
    # i*2: head
    # i*2+1: feet
    
    graph = [[0] * (2*N+2) for _ in range(2*N+2)]
    for v1, v2 in edges:
        # Head connect feet
        graph[2*v1][2*v2+1] = 1
        graph[2*v2][2*v1+1] = 1
    
    source = 0
    sink = 1
    
    # Source connect to each head
    for i in range(1, N+1):
        head = 2*i
        graph[source][head] = min(T, sum(graph[head]))
    
    # Each feet connect to sink
    for i in range(1, N+1):
        feet = 2*i+1
        graph[feet][sink] = 1
    
    # --- Graph Completed ---
    # Now run Flow Alg.
    g = Graph(graph)
    ans = g.FordFulkerson(source, sink)
    return ans
    
    
    
    
    

if __name__ == '__main__':
    c = int(input().strip())

    for c_itr in range(c):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        t = int(first_multiple_input[1])

        m = int(first_multiple_input[2])

        graph = []

        for _ in range(m):
            graph.append(list(map(int, input().rstrip().split())))

        result = crabGraphs(n, t, graph)
        print(result)