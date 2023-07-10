
T = int(input())

for _ in range(T):
    X, Y, Z = map(int, input().split())
    credits = 4 * X + 2 * Y
    print(credits)
