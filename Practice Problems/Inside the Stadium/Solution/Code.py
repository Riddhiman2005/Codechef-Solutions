# Read the number of test cases
T = int(input())

# Iterate over each test case
for _ in range(T):
    # Read the total number of balls played by Gill
    N = int(input())

    # Read the runs scored on each ball
    A = list(map(int, input().split()))

    # Initialize the counter
    count = 0

    # Iterate over the runs scored on each ball
    for i in range(N):
        # Calculate the strike rate for the current ball
        strike_rate = (sum(A[:i+1]) / (i+1)) * 100

        # Check if the strike rate equals 100
        if strike_rate == 100:
            count += 1

    # Print the number of times the strike rate became exactly 100
    print(count)
