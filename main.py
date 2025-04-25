from sorting import insertion_sort, selection_sort, merge_sort, quick_sort
from searching import binary_search
from greedy import Graph, dijkstra, knapsack

g = Graph(5)
g.graph = [
    [0, 4, 2, 0, 0],
    [0, 0, 3, 2, 3],
    [0, 1, 0, 4, 5],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0]
]
dijkstra(g, 0)

print("Vertex\tDistance from Source\tParent")
for v in range(g.V):
    print(f"{v}\t{g.distances[v]}\t\t\t{g.parents[v]}")
    
print(knapsack([60, 100, 120], [10, 20, 30], 50))