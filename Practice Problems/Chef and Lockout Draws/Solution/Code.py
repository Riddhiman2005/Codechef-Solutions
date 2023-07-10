
def canMatchEndInDraw(A, B, C):
    return (A + B + C) % 2 == 0 and (A == B or B == C or C == A)

T = int(input())

for _ in range(T):
    A, B, C = map(int, input().split())
    result = "YES" if canMatchEndInDraw(A, B, C) else "NO"
    print(result)
