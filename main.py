from sorting import insertion_sort, selection_sort, merge_sort, quick_sort
from searching import binary_search
from greedy import Graph, dijkstra, knapsack
from dynamic_programming import fibonacci, LongestCommonSubsequence
from backtracking import solve_n_queens
from string_matching import naive

A = [12, 3, 7, 9, 14, 6, 11, 2]
print(f"Array before sort: {A}")
merge_sort(A, 0, len(A) - 1)
print(f"Array after merge sort: {A}")

print("=" * 50)

B = [12, 3, 7, 9, 14, 6, 11, 2]
print(f"Array before sort: {A}")
quick_sort(B, 0, len(B) - 1)
print(f"Array after quick sort: {B}")

print("=" * 50)

lcs = LongestCommonSubsequence("stone", "longest")
print("Using Tabulation: ", lcs.tabulation())
print("Longest Common Subsequence: ", lcs.print_lcs())

print("=" * 50)

solutions = solve_n_queens(4)
print(f"For the 4-Queens problem, here are the {len(solutions)} possible solutions")
for i, solution in enumerate(solutions):
    for row in solution:
        print(row)
    print()

print("=" * 50)

text = "ABAAABCDBBABCD"
pattern = "ABC"
indices = naive(text, pattern)
print(f"Pattern {pattern} found at indices: {indices}")