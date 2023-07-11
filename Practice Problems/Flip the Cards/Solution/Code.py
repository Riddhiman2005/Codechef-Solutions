# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the input for each test case
    N, X = map(int, input().split())

    # Calculate the minimum number of operations
    operations = min(X, N - X)

    # Print the minimum number of operations
    print(operations)
