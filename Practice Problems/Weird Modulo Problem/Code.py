t = int(input())

while t:
    N = int(input())
    A = list(map(int, input().split()))
    m = float('inf')  # Initialize 'm' with positive infinity
    
    for i in range(N):
        A[i] = int(A[i])
        if A[i] < m:
            m = A[i]
    
    print(m)
    
    t -= 1
