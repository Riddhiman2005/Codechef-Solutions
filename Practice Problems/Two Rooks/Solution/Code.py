def areRooksAttacking(x1, y1, x2, y2):
    return x1 == x2 or y1 == y2

T = int(input())

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    result = "YES" if areRooksAttacking(x1, y1, x2, y2) else "NO"
    print(result)
