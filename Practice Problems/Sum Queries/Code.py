n,m=map(int,input().split())
while(m>0):
    q=int(input())
    if n+2<=q<=3*n:
        index=abs(n-q)
        if index<=n:
            print(index-1)
        else:
            print(2*n+1-index)
    else:
        print(0)
    m=m-1
