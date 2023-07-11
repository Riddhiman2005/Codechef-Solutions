# Read the number of test cases
T = int(input())

# Iterate over each test case
for _ in range(T):
    # Read the number of days
    N = int(input())

    # Read the distances run by Alice and Bob on each day
    Alice_distances = list(map(int, input().split()))
    Bob_distances = list(map(int, input().split()))

    # Initialize the counter
    happy_days = 0

    # Iterate over the distances run on each day
    for i in range(N):
        # Check if both Alice and Bob are happy on the current day
        if Alice_distances[i] <= 2 * Bob_distances[i] and Bob_distances[i] <= 2 * Alice_distances[i]:
            happy_days += 1

    # Print the number of days when both Alice and Bob were happy
    print(happy_days)
