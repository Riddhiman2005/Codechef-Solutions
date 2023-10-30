import math
for _ in range(int(input())):
    a,b = map(int,input().split())
    if a == 1 or b ==1:
            print(-1)
    elif math.gcd(a,b) == 1:
        print(1)
    else:
        print(0)
        
        
