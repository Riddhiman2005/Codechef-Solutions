
# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the size of the group and the cost of one subscription
    n, x = map(int, input().split())

    # Calculate the minimum total cost
    subscriptions = (n + 5) // 6  # Round up to the nearest multiple of 6
    total_cost = subscriptions * x

    # Print the minimum total cost
    print(total_cost)
