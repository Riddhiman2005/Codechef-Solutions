mod = 998244353
lim = 2 * 10**6 + 20
fac = [1] + [i for i in range(1, lim)]
for i in range(1, lim):
    fac[i] = fac[i-1] * i % mod
invf = [0]*lim
invf[-1] = pow(fac[-1], mod-2, mod)
for i in reversed(range(lim-1)):
    invf[i] = invf[i+1] * (i+1) % mod
def C(n, r):
    if n < r or r < 0:
        return 0
    return fac[n] * invf[r] % mod * invf[n-r] % mod
def calc(k, n):
    if k == 0:
        return 1 if n == 0 else 0
    return C(n+k-1, n)
T = int(input())
for _ in range(T):
    n, m, d, k = map(int, input().split())
    ans = 0
    k -= d
    for i in range(n):
        if i*d > k:
            break
        ways = C(n-1, i) * calc(i+2, m-1-k) % mod
        sm, sign = 0, 1
        for j in range(n-i):
            if k - i*d - j*d < 0:
                break
            sm += C(n-1-i, j) * calc(n-1-i, k - i*d - j*d) % mod * sign % mod
            sign *= -1
        ans += ways * sm % mod
    print(ans % mod)
