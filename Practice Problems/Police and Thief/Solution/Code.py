# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the input for each test case
    X, Y = map(int, input().split())

    # Calculate the minimum time using the formula: time = abs(X - Y) / (2 - 1)
    time = abs(X - Y) / 1

    # Print the minimum time
    print(int(time))

