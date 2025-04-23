def selection_sort(A):
    n = len(A)
    for i in range(n - 1):
        min = i
        print(f"\n\nAt Iteration {i}, we have the following array: {A}")
        print(f"The minimum value in the array is {A[min]}")
        
        for j in range(i + 1, n):
            if (A[j] < A[min]):
                min = j
                print(f"\n\nAt Iteration {i}, Pass {j}, we found a new minimum value at {min} i.e. {A[min]}")
        
        if (min != i):
            print(f"\nSwapping {A[min]} and {A[i]}")
            A[min], A[i] = A[i], A[min]