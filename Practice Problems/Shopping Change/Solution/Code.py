
# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the total price of items
    x = int(input())

    # Calculate the amount of money Chef should receive back
    change = 100 - x

    # Print the change
    print(change)
