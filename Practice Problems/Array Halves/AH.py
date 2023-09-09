for _ in range(int(input())):
    n = int(input())
    P = list(map(int, input().split()))
    
    Q = sorted(P)
    mid_val = Q[n-1]
    ans = 0
    curr = n
    i = 0
    while i < curr:
        if P[i] > mid_val:
            ans += (curr - i)
            curr += 1
        i += 1
    
    print(ans)
