
# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the input for each test case
    N = int(input())

    # Calculate the minimum number of 1's required
    min_ones = (N + 1) // 2

    # Print the result
    print(min_ones)
