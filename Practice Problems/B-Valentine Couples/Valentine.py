import sys
import bisect
input=lambda: sys.stdin.readline().strip("\r\n")
from math import log
from math import gcd
sys.setrecursionlimit(10**6)
flsh=lambda: sys.stdout.flush()
sa=lambda :input()
sb=lambda:int(input())
sc=lambda:input().split()
sd=lambda:list(map(int,input().split()))
se=lambda:float(input())
sf=lambda:list(input())
mod=10**9+7
def P():
    n=sb()
    a=sd()
    b=sd()
    a.sort()
    b.sort(reverse=True)
    max_=0
    for i in range(n):
        max_=max(max_,a[i]+b[i])
    print(max_)
for _ in range(sb()):
    P()
