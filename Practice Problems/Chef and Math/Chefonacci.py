def chefonacci(n):
    chef = [1, 2] 
    for val in range(2, n):
        chef.append(chef[val-1] + chef[val-2])
    return chef

def F(x, k, n, chef):
    if k > 0 and x < k * chef[0] and x >= 0:
        return 0
    if x < 0:
        return 0
    if k == 1:
        for val in chef:
            if val == x:
                return 1
        return 0
    if k == 0:
        if x == 0:
            return 1
        else:
            return 0
    elif x == 0 or n == 0:
        return 0
    else:
        total = F(x, k, n-1, chef)
        if x >= chef[n-1] and x <= k * chef[n-1]:
            total += F(x - chef[n-1], k - 1, n, chef)
        return total

chef = chefonacci(44)
Q = int(input())
for case in range(Q):
    X, K = list(map(int, input().split()))
    number = F(X, K, 43, chef)
    print(number)
