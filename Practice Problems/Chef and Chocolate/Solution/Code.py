
# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the values of C, X, and Y
    c, x, y = map(int, input().split())

    # Calculate the minimum money Chef needs to spend
    minimum_money = max(0, (c - x) * y)

    # Print the result
    print(minimum_money)
