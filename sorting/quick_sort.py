def quick_sort(A, low, high):
    if low < high:
        pivot = partition(A, low, high)
        
        quick_sort(A, low, pivot - 1)
        quick_sort(A, pivot + 1, high)

def partition(A, low, high):
    pivot = A[low]
    i, j = low, high
    
    while i < j:
        while A[i] <= pivot and i <= high - 1:
            i += 1
        while A[j] >= pivot and j >= low + 1:
            j -= 1
        
        if (i < j):
            A[i], A[j] = A[j], A[i]
    
    A[low], A[j] = A[j], A[low]
    return j

if __name__ == "__main__":
    A = [30, 10, 50, 20, 40]
    print(f"Array before quick sort: {A}")
    quick_sort(A, 0, len(A) - 1)
    print(f"Array after quick sort: {A}")
