for _ in range(int(input())):
    #code goes here
    n = int(input())
    a = list(map(int,input().split()))
    cnt = a[n-1]
    t = a[n-1]
    for i in range(n-2,-1,-1):
        if((t-1)<(a[i])):
            cnt += (a[i] - (t-1))
        t = a[i]
    print(cnt)
