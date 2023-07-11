
# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the cost of a double room and a triple room
    X, Y = map(int, input().split())

    # Calculate the minimum amount required
    amount1 = 3 * X  # Cost of three double rooms
    amount2 = 2 * Y  # Cost of two triple rooms

    # Print the minimum amount
    print(min(amount1, amount2))
