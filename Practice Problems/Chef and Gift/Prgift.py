for _ in xrange(input()):
    n, k = map(int, raw_input().split())
    A = map(int, raw_input().split())
    c = 0
    for i in xrange(n):
        if A[i] % 2 == 0:
            c += 1
    if k == 0 and c == n:
        print "NO"
    elif c >= k:
        print "YES"
    else:
        print "NO"
