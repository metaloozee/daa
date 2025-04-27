def merge_sort(A, low, high):
    if (low >= high):
        return

    mid = (low + high) // 2
    merge_sort(A, low, mid)
    merge_sort(A, mid + 1, high)
    merge(A, low, mid, high)


def merge(A, low, mid, high):
    tmp = []
    left = low
    right = mid + 1

    while left <= mid and right <= high:
        if A[left] <= A[right]:
            tmp.append(A[left])
            left += 1
        else:
            tmp.append(A[right])
            right += 1

    while left <= mid:
        tmp.append(A[left])
        left += 1
    while right <= high:
        tmp.append(A[right])
        right += 1
    
    for i in range(len(tmp)):
        A[low + i] = tmp[i]
