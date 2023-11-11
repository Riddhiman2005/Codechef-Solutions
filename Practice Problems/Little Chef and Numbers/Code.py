for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    count2 = 0
    count3 = 0
    ans = 0 
    for i in range(len(a)-1,-1,-1):
        if a[i] > 2:
            ans += count2
            ans += count3
            count3 +=1
        elif a[i] == 2:
            ans += count3
            count2 +=1
    print(ans)
