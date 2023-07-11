# Read the number of test cases
T = int(input())

# Iterate over each test case
for _ in range(T):
    # Read the values for N, X, and K
    N, X, K = map(int, input().split())

    # Calculate the maximum number of bottles Chef can fill completely
    max_bottles = min(N, K // X)

    # Print the result
    print(max_bottles)
