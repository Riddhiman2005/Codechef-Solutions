def same_string_guaranteed(A, B):
    return A == B


# Input
T = int(input())

for _ in range(T):
    N = int(input())
    S = input()
    A = S[:N//2]
    B = S[N//2:]

    result = same_string_guaranteed(A, B)

    if result:
        print("YES")
    else:
        print("NO")
