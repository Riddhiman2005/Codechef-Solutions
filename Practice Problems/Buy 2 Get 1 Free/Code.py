
# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the values of N and X
    N, X = map(int, input().split())

    # Calculate the number of sets and the remaining items
    sets = N // 3
    remaining_items = N % 3

    # Calculate the cost of the sets and the remaining items
    set_cost = sets * (2 * X)
    remaining_cost = remaining_items * X

    # Calculate the total minimum money required
    total_cost = set_cost + remaining_cost

    # Print the result
    print(total_cost)
