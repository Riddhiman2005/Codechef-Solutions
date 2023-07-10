
T = int(input())

for _ in range(T):
    X, Y = map(int, input().split())
    donation_amount = Y - X
    print(donation_amount)
