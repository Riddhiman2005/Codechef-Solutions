t=int(input())
for _ in range(t):
    k=input().split()
    n,m,h=int(k[0]),int(k[1]),int(k[2])
    l=list(map(int,input().split()))
    a=list(map(int,input().split()))
    l.sort(reverse=True)
    a.sort(reverse=True)
    res=0
    for i in range(n if n<m else m):
        res+=min(l[i],a[i]*h)
    print(res)
