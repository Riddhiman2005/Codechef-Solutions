T = int(input())
for t in range (T):
    N = int(input())
    A = input()
    C = input()
    W = list(map(int, input().split()))
    c = 0
    m = W[0]
    for i in range (N):
        if (A[i] == C[i]):
            c += 1
        if (W[c] > m):
            m = W[c]
    if (N == c):
        print(W[N])
    else:
        print(m)
