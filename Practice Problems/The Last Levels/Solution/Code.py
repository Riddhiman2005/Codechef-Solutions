# Read the number of test cases
T = int(input())

# Iterate over each test case
for _ in range(T):
    # Read the values for X, Y, Z
    X, Y, Z = map(int, input().split())

    # Calculate the total time
    total_time = (X * Y) + ((X - 1) // 3) * Z

    # Print the total time
    print(total_time)
