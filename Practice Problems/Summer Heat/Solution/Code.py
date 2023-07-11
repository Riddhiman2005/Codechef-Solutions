
# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the coconut quantities
    x_a, x_b, X_a, X_b = map(int, input().split())

    # Calculate the minimum number of coconuts required
    num_A = (X_a + x_a - 1) // x_a  # Round up to the nearest integer
    num_B = (X_b + x_b - 1) // x_b  # Round up to the nearest integer

    # Print the total number of coconuts required
    print(num_A + num_B)
