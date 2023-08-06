# cook your dish here
t = int(input())

while t > 0:
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    divisor = 1
    for i in range(n):
        divisor *= a[i]

    for i in range(q):
        if divisor == 0:
            print("0", end=" ")
        else:
            print(b[i] // divisor, end=" ")

    print()
    t -= 1
