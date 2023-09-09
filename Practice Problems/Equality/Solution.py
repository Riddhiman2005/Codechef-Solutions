# cook your dish here
T = int(input())

for _ in range(T):
    n = int(input())
    
    solution = list(map(int, input().split()))
    
    x = sum(solution) // (n - 1)
    
    for i in range(len(solution)):
        print(x - solution[i], end = " ")
    print()
