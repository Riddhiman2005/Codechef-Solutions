T = int(input())

for _ in range(T):
    n, x = map(int, input().split())
    
    if n % 2 == 1:
        print(x, end = ' ')
    
    for i in range(n // 2):
        print(x - (i + 1), x + (i + 1), end = ' ')
    print()
