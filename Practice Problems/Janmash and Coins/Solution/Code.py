
# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the number of 10 rupee coins and 5 rupee coins
    x, y = map(int, input().split())

    # Calculate the total money Janmansh has
    total_money = (x * 10) + (y * 5)

    # Print the total money
    print(total_money)
