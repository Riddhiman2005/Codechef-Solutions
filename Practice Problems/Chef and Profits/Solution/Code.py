
# Read the number of test cases
T = int(input())

# Iterate over each test case
for _ in range(T):
    # Read the number of stocks, buying price, and selling price
    X, Y, Z = map(int, input().split())

    # Calculate Chef's profit
    profit = X * (Z - Y)

    # Print the profit
    print(profit)
