t=int(input())
for _ in range(t):
    l,r=map(int,input().split())
    if(l>r):
        print(-1)
    elif(l*2>r):
        print(r)
    else:
        print(-1)
