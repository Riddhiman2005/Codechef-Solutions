# cook your dish here
T = int(input())

for _ in range(T):
    N, M, K = [int(x) for x in input().split()]

    if N + M <= 3: 
        print(0)
    elif N == 1 or M == 1:
        print(K)
    else:
        print((K + 1) // 2)
