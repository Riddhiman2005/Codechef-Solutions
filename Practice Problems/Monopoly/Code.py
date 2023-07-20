def has_monopoly(P, Q, R, S):
    total_profit = P + Q + R + S
    max_profit = max(P, Q, R, S)
    return max_profit > total_profit - max_profit

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    P, Q, R, S = map(int, input().split())
    if has_monopoly(P, Q, R, S):
        print("YES")
    else:
        print("NO")
