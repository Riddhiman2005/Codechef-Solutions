t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    
    m1=min(l)
    m2=max(l)
    
    if(n==1):
        print("yes")
    elif(m2>=k):
        print("NO")
    elif((m1+m2)<=k):
        print("Yes")
    else:
        print("NO")
