def binary_search(A, p, q, num):
    if (p > q):
        return print(f"{num} does not exist")

    mid = (p + q) // 2
    if A[mid] == num:
        return print(f"{num} found at index {mid}")
    elif A[mid] > num:
        return binary_search(A, p, mid - 1, num)
    else:
        return binary_search(A, mid + 1, q, num)