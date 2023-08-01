def can_make_equal(A, B):
    diff = abs(A - B)
    if diff % 2 == 0:
        return "YES"
    else:
        return "NO"

# Input
T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    result = can_make_equal(A, B)
    print(result)
