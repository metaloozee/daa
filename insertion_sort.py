def insertion_sort(A):
    n = len(A)
    print(f"Length of our array: {A} is {n}")
    
    for i in range(1, n):
        print(f"\nAt Iteration {i}, we have the following array: {A}")
        key = A[i]
        j = i - 1
        
        print(f"The key value is {key}")
        
        while j >= 0 and A[j] > key:
            print(f"Since {A[j]} > {key}, we shift {A[j]} to the right")
            A[j + 1] = A[j]
            j = j - 1
            
        A[j + 1] = key
        print(f"We insert {key} at position {j + 1}")
A = [7, 10, 3, 5, 2, 6, 1]
insertion_sort(A)

print(f"\n\nThe final sorted array is: {A}")
