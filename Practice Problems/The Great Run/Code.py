
# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the length of the track and the maximum distance Vishal can run
    N, K = map(int, input().split())

    # Read the number of girls within each kilometre of the track
    girls = list(map(int, input().split()))

    # Initialize the maximum number of girls Vishal can impress
    max_girls = 0

    # Iterate over each possible segment of length K
    for i in range(N - K + 1):
        # Calculate the total number of girls in the current segment
        total_girls = sum(girls[i:i+K])

        # Update the maximum number of girls if necessary
        max_girls = max(max_girls, total_girls)

    # Print the maximum number of girls Vishal can impress
    print(max_girls)
