t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    is_invalid = False
    is_weak = False
    for _ in range(n):
        intended, result = input().split()
        if intended == 'correct':
            if result.count('0'):
                is_invalid = True
        elif intended == 'wrong':
            if not result.count('0'):
                is_weak = True
        else:
            assert False
    if is_invalid:
        answer = 'INVALID'
    elif is_weak:
        answer = 'WEAK'
    else:
        answer = 'FINE'
    print(answer)
