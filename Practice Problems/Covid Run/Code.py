t = int(input())
for i in range(t):
    inputs = input().split()
    n = int(inputs[0])
    k = int(inputs[1])
    x = int(inputs[2])
    y = int(inputs[3])
    if x == y:
        print("YES")
        break
    spread = x
    while True:
        spread = (spread + k) % n
        if spread == y:
            print("YES")
            break
        elif spread == x:
            print("NO")
            break
