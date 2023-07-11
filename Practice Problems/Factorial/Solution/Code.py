
# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the value of N
    N = int(input())

    # Initialize the count of zeros
    zeros_count = 0

    # Calculate the number of trailing zeros
    while N >= 5:
        N //= 5
        zeros_count += N

    # Print the count of trailing zeros
    print(zeros_count)
