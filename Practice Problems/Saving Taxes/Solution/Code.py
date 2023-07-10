
# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the earnings and tax threshold
    X, Y = map(int, input().split())

    # Calculate the minimum amount to invest
    minimum_investment = max(0, X - Y)

    # Print the result
    print(minimum_investment)
