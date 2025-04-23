from sorting import insertion_sort, selection_sort, merge_sort, quick_sort

A = [12, 3, 7, 9, 14, 6, 11, 2]
print("Array before sort: ", A)
quick_sort(A, 0, len(A) - 1)
print("Array after sort: ", A)