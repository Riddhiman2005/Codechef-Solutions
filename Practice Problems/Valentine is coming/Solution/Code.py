# Read the number of test cases
T = int(input())

# Iterate over each test case
for _ in range(T):
    # Read the values for X and Y
    X, Y = map(int, input().split())

    # Calculate the maximum number of chocolates Chef can buy
    max_chocolates = X // Y

    print(max_chocolates)
