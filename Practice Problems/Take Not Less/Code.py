def f():
    n=int(input())
    a=map(int,input().split())
    d={}
    for i in a:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    for i in d.values():
        if i%2!=0:
            return 'Marichka'
    return 'Zenyk'
for _ in range(int(input())):
    print(f())
