import math

def lcm(a, b):
    return (a * b) // math.gcd(a, b)

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    result = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            result = min(result, lcm(arr[i], arr[j]))
    print(result)
