# cook your dish here
import math
T = int(input())
for _ in range(T):
    n,k = map(int,input().split())
    
    if k <= n:
        ans = k
    else:
        ans = n
        k -= n
        i = 1
        j = 1
        while k > 0:
            if (2*j)*n <= k:
                ans += n
                k -= (2*j)*n
                j *= 2
                i += 1
            else:
                ans += k//(2*j)
                k  -= (k//(2*j))*(2*j)
                a = 2**i - 1
                x = str(bin(a))
                a += k
                y = str(bin(a))
                ans += y.count("1") - x.count("1")
                k = 0
    print(ans)
