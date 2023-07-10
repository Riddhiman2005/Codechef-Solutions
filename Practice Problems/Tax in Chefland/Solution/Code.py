
# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the total income
    X = int(input())

    # Check if total income is greater than 100
    if X > 100:
        money_received = X - 10
    else:
        money_received = X

    # Print the result
    print(money_received)
