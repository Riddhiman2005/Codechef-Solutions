T = int(input())
while T:
    T -= 1
    D, d, P, Q = map(int, input().split())
    res = ((d * (D // d) * (2 * P + ((D // d) - 1) * Q)) // 2) + ((D % d) * (P + (D // d) * Q))
    print(res)
