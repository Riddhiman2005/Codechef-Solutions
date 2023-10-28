T = int(input())
while T:
    T -= 1
    N = int(input())
    L = list(map(int, input().split()))
    min = L[0]
    max = 0
    for i in range(N):
        if L[i] < min:
            min = L[i]
        elif L[i] - min > max:
            max = L[i] - min
    if max > 0:
        print(max)
    else:
        print("UNFIT")
