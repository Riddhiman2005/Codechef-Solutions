# cook your dish here
import sys
sys.setrecursionlimit(10 ** 6)

for t in range(int(input())):
    N = int(input())
    g = [[] for i in range(N + 1)]
    for i in range(N - 1):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
    A = [None] + [bin(int(Ai)).count('1') % 2 for Ai in input().split()]
    cnt = [[0, 0], [0, 0]]
    def dfs(u, p, d):
        cnt[A[u]][d] += 1
        for v in g[u]:
            if v != p:
                dfs(v, u, d ^ 1)
    dfs(1, 1, 0)
    ans = (cnt[0][0] + cnt[1][1]) * (cnt[0][1] + cnt[1][0])
    print(ans)
