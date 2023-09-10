import sys
import bisect
from bisect import bisect_left as lb
from bisect import bisect_right as rb
input_=lambda: sys.stdin.readline().strip("\r\n")
from math import log
from math import gcd
from math import atan2,acos
from random import randint
sa=lambda :input_()
sb=lambda:int(input_())
sc=lambda:input_().split()
sd=lambda:list(map(int,input_().split()))
sflo=lambda:list(map(float,input_().split()))
se=lambda:float(input_())
sf=lambda:list(input_())
flsh=lambda: sys.stdout.flush()
mod=10**9+7
mod1=998244353
gp=[]
cost=[]
dp=[]
mx=[]
ans1=[]
ans2=[]
special=[]
specnode=[]
a=0
kthpar=[]
def dfs2(root,par):
    if par!=-1:
        dp[root]=dp[par]+1
    for i in range(1,20):
        if kthpar[root][i-1]!=-1:
            kthpar[root][i]=kthpar[kthpar[root][i-1]][i-1]
    for child in gp[root]:
        if child==par:continue
        kthpar[child][0]=root
        dfs(child,root)
        
ans=0
a=[]
n,k=0,0
b=[]
vis=[]
tot=0
time=[]
time1=[]
adj=[]
mx=-1
eps=0.0000001
gp=[]
ans=[]
def update_it(bit,i,val):
    n=len(bit)
    while(i<n):
        bit[i]+=val
        i+=i&(-i)
def get_ans(bit,i):
    n=len(bit)
    tot=0
    while(i>0):
        tot+=bit[i]
        i-=i&(-i)
    return tot
def flip(a,l,r):
    for i in range(l,r):
        a[i]='0' if a[i]=='1' else '1'
    return
def hnbhai(tc):
    n=sb()
    a=sd()
    pos=[]
    neg=[]
    for i in range(n):
        if i%2==0:
            pos.append(abs(a[i]))
        else:
            neg.append(abs(a[i]))
    pos.sort()
    neg.sort(reverse=True)
    print(max(sum(pos)-sum(neg)+2*neg[0]-2*pos[0],sum(pos)-sum(neg)))
    return
for _ in range(sb()):
    hnbhai(_+1)
