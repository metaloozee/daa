from sorting import insertion_sort, selection_sort, merge_sort, quick_sort
from searching import binary_search
from greedy import Graph, dijkstra, knapsack
from dynamic_programming import fibonacci

f = fibonacci()

print("Using traditional Recursion: ", f.recursion(10))
print("Using Memoization: ", f.memo(10))
print("Using Tabulation: ", f.tabulation(10))