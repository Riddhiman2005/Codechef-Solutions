def is_investment_good(X, Y):
    return X >= 2 * Y

# Input
T = int(input())

for _ in range(T):
    X, Y = map(int, input().split())

    # Check if the investment is good and print the result
    result = "YES" if is_investment_good(X, Y) else "NO"
    print(result)
