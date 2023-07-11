# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the amount to be paid
    X = int(input())

    # Check if X is divisible by 10
    if X % 10 == 0:
        # If divisible, no coins needed
        coins = 0
    else:
        # If not divisible, number of coins required is X mod 10
        coins = X % 10

    # Print the minimum number of coins required
    print(coins)
