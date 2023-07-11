
# Read the number of test cases
T = int(input())

# Define the denominations
denominations = [100, 50, 10, 5, 2, 1]

# Process each test case
for _ in range(T):
    # Read the sum of Rs. N
    N = int(input())

    # Initialize the count of notes
    count = 0

    # Compute the smallest number of notes
    for denom in denominations:
        count += N // denom
        N %= denom

    # Print the result
    print(count)
