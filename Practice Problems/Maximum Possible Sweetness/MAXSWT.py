import bisect

def solve(a, b, n, d):
    mat = sorted([[a[i], b[i]] for i in range(n)])
    dp = [0]*n
    aa = [0]*n
    for i in range(n):
        aa[i] = mat[i][0]
        dp[i] = mat[i][1]
    for i in range(1, n):
        dp[i] = max(dp[i], dp[i - 1])
    ans = 0
    for i in range(n - 1, 0, -1):
        if mat[i][0] < d:
            re = d - mat[i][0]
            ind = bisect.bisect_right(aa, re)
            if ind == 0:
                ans = max(ans, dp[i])
            else:
                ind = min(i - 1, ind - 1)
                ans = max(ans, mat[i][1] + dp[ind])
        if mat[i][0] == d:
            ans = max(ans, mat[i][1])
    if mat[0][0] <= d:
        ans = max(ans, mat[0][1])
    return ans




for _ in range(int(input())):
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solve(a, b, n, d))
