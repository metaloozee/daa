def merge_sort(A, p, r):
    if (p >= r):
        return
    q = (p + r) // 2
    merge_sort(A, p, q)
    merge_sort(A, q + 1, r)
    merge(A, p, q, r)


def merge(A, p, q, r):
    nL = q - p + 1
    nR = r - q
    L = A[p: p + nL]
    R = A[(q+1): (q+1) + nR]
    i, j = 0, 0
    k = p
    while i < nL and j < nR:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    while i < nL:
        A[k] = L[i]
        i += 1
        k += 1
    while j < nR:
        A[k] = R[j]
        j += 1
        k += 1
