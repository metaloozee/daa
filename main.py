from lib.merge_sort import merge_sort

A = [12, 3, 7, 9, 14, 6, 11, 2]
print("Array before merge_sort: ", A)
merge_sort(A, 0, len(A) - 1)
print("Array after merge_sort: ", A)