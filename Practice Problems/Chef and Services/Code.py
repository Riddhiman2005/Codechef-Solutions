# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the input values
    P1, P2, K = map(int, input().split())

    # Calculate the total points scored
    total_points = P1 + P2

    # Determine if it is Chef's or Cook's turn to serve
    if (total_points // K) % 2 == 0:
        print("CHEF")
    else:
        print("COOK")
