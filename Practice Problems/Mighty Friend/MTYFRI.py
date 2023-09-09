t=int(input())
while(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    z=l[0:n:2]
    y=l[1:n:2]
    z.sort(reverse=True)
    y.sort()
    i=0
    temp=0
    m=0
    while(i<n//2 and m<k):
        if z[i]>y[i]:
            temp=z[i]
            z[i]=y[i]
            y[i]=temp
            m+=1
        i+=1
    if sum(y)>sum(z):
        print('YES')
    else:
        print('NO')
    t=t-1
        
