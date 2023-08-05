t = int(input())

for _ in range(t):
    N = int(input())
    A = list(map(int, input().split()))

    sum_chapters = sum(A)
    flag = 0

    for i in range(N):
        if A[i] == i + 1:
            flag += 1

    if flag != N and sum_chapters == N * (N + 1) // 2:
        print("yes")
    else:
        print("no")
