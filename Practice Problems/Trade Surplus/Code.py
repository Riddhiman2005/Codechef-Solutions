for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    x=a-b
    y=c-d
    z=x+y
    if(z<0):
        print("YES")
    else:
        print("No")
