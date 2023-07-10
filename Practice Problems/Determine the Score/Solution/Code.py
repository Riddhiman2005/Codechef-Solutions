
# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read X and N
    X, N = map(int, input().split())

    # Calculate the points scored by Chef
    points = X * N // 10

    # Print the result
    print(points)
