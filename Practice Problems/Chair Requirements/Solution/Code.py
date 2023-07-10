
T = int(input())

for _ in range(T):
    X, Y = map(int, input().split())
    if X > Y:
        extra_chairs = X - Y
        print(extra_chairs)
    else:
        print(0)
