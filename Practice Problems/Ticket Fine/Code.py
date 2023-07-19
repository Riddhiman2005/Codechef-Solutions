# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    # Read the fine amount, number of passengers, and number of tickets collected
    X, P, Q = map(int, input().split())

    # Calculate the number of passengers without a ticket
    passengers_without_ticket = P - Q

    # Calculate the total fine collected
    total_fine = passengers_without_ticket * X

    # Print the total fine collected for the current test case
    print(total_fine)
