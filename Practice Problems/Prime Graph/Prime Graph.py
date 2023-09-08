from sys import stdin, stdout
input = stdin.readline
import bisect

all=[]

def SieveOfEratosthenes(n):
    global all
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if prime[p]:
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    for p in range(2, n+1):
        if prime[p]:
            all.append(p)

SieveOfEratosthenes(10**5+5)

t = int(input())
for _ in range(t):
    n=int(input())
    ind=bisect.bisect_left(all,n-1)
    if all[ind]!=n-1:
        ind-=1
    if n%2==0 or all[ind]%2==0:
        print((n*all[ind])//2)
    else:
        print(((n-1)*all[ind]+2)//2)
