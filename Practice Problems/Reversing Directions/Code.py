T = int(input())
for _ in range(T):
    n = int(input())
    u = [0] * n
    s = [0] * n
    for i in range(n):
        x = input()
        u[i] = x[0]
        if x[0] == 'L':
            s[i] = x[8:]
        else:
            s[i] = x[9:]
    print('Begin on', s[n - 1])  
    for i in range(n - 1, 0, -1):
        if u[i] == 'L':
            print('Right on', s[i - 1])
        else:
            print('Left on', s[i - 1])
