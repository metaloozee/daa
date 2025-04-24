import heapq
from .graph import Graph

def initialize_single_source(G: Graph, source):
    for vertex in range(G.V):
        G.distances.update({vertex: float('inf')})
        G.parents.update({vertex: None})
    G.distances.update({source: 0})
    
    
def relax(G: Graph, u, v):
    weight = G.graph[u][v]
    if weight and G.distances[v] > G.distances[u] + weight:
        G.distances[v] = G.distances[u] + weight
        G.parents[v] = u
        return True
    return False

def dijkstra(G: Graph, source):
    initialize_single_source(G, source)
    
    visited = set() 
    heap = [(0, source)] 
    
    while heap:
        dist_u, u = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)
        for v in range(G.V):
            if G.graph[u][v] and v not in visited:
                if relax(G, u, v):
                    heapq.heappush(heap, (G.distances[v], v))