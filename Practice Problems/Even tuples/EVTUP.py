import os.path
from math import gcd, floor, ceil
from collections import *
import sys
from random import *
mod = 1000000007
INF = float('inf')
def st(): return list(sys.stdin.readline().strip())
def li(): return list(map(int, sys.stdin.readline().split()))
def mp(): return map(int, sys.stdin.readline().split())
def inp(): return int(sys.stdin.readline())
def pr(n): return sys.stdout.write(str(n)+"\n")
def prl(n): return sys.stdout.write(str(n)+" ")


if os.path.exists('input.txt'):
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')


def solve():
    n, q = mp()
    l = li()
    eve = [0]
    odd = [0]
    for i in range(n):
        if l[i] % 2:
            eve.append(eve[-1])
            odd.append(odd[-1]+1)
        else:
            eve.append(eve[-1]+1)
            odd.append(odd[-1])
    for i in range(q):
        a, b = mp()
        evens = eve[b]-eve[a-1]
        odds = odd[b]-odd[a-1]
        ans = (evens*(evens-1)*(evens-2))//6
        ans += ((odds*(odds-1))//2)*evens
        pr(ans)


for _ in range(inp()):
    solve()
