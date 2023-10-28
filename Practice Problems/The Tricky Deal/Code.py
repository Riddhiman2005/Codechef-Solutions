T = int(input())

for _ in range(T):
    a = int(input())
    tot = 0
    m = 0
    setm = 0
    out = 1
    d = 0
    while 1:
        if out >= a and setm == 0:
            setm = 1
            m = d
            
        tot += (a - out)
        if tot <= 0 and d:
            print(d, m)
            break
        out *= 2
            
        d += 1
