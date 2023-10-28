import math
t = int(input())
for i in range(t):
    n = int(input())
    j = 2
    ans = [1]
    while j<math.sqrt(n):
        if n%j==0:
            ans.append(j)
            ans.append(n//j)
            break
        j+=1
    if len(ans)>1:
        print(*ans)
    else:
        print(-1)
    
