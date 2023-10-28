for i in range(int(input())):
    a=int(input())
    l=list(map(int,input().split()))
    l.sort(reverse=True)
    s=0
    for i in range(a):
        if i%2==0:
            s+=l[i]
    print(s)
