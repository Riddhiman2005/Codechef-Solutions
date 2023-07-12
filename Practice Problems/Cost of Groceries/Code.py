
# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the number of items and the minimum freshness value
    N, X = map(int, input().split())

    # Read the freshness values and costs of the items
    freshness = list(map(int, input().split()))
    cost = list(map(int, input().split()))

    # Calculate the total cost of the groceries Chef buys
    total_cost = 0
    for i in range(N):
        if freshness[i] >= X:
            total_cost += cost[i]

    # Output the result
    print(total_cost)
