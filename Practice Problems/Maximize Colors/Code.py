T = int(input())
while T:
    T -= 1
    X, Y, Z = map(int, input().split())
    c = 0

    if X > 0:
        c += 1

    if Y > 0:
        c += 1

    if Z > 0:
        c += 1
    
    X_remain = X - 1
    Y_remain = Y - 1
    Z_remain = Z - 1
    r = [X_remain, Y_remain, Z_remain]
    r.sort()

    if r[0] >= 2:
        c += 3
    elif r[0] == 1 and r[2] >= 2:
        c += 2
    elif r[1] >= 1:
        c += 1
    print(c)
