import sys
import math
import bisect
from sys import stdin, stdout
from math import gcd, floor, sqrt, log2, ceil
from collections import defaultdict as dd
from bisect import bisect_left as bl, bisect_right as br
from bisect import insort
from collections import Counter
from collections import deque
from heapq import heappush,heappop,heapify
from itertools import permutations,combinations
from itertools import accumulate as ac
from random import randint as ri
mod = int(1e9)+7
#mod = 998244353
 
ip = lambda : int(stdin.readline())
inp = lambda: map(int,stdin.readline().split())
ips = lambda: stdin.readline().rstrip()
out = lambda x : stdout.write(str(x)+"\n")


#change response for CreateRoom
#firebase oppenent update entry
#room save api , add parameter call time
#opponent team left 

def prime(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    return prime


t = ip()
for _ in range(t):
    n,k = inp()
    a = []
    b = []
    pr = prime(n+1)
    st = n//2 + 1
    for i in range(2,st):
        a.append(i)
    for i in range(st,n+1):
        if pr[i]:
            b.append(i)
        else:
            a.append(i)

    sta = list(a)
    stb = list(b)

    b.append(1)
    f = False

    while b:
        if k == len(a):
            f = True
            ans = a
            break
        else:
            if k == len(b):
                f = True
                ans = b
                break
            else:
                a.append(b.pop())
        

    a = list(sta)
    b = list(stb)
    a.append(1)

    while b:
        if k == len(a):
            f = True
            ans = a
            break
        else:
            if k == len(b):
                f = True
                ans = b
                break
            else:
                a.append(b.pop())

    if f:
        print("Yes")
        ans.sort()
        print(*ans)
    else:
        print("No")
