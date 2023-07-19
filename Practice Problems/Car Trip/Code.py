# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    # Read the number of kilometers traveled
    X = int(input())

    # Calculate the cost
    if X >= 300:
        cost = X * 10
    else:
        cost = 3000  # Since Chef needs to pay for at least 300 kms

    # Print the cost for the current test case
    print(cost)
