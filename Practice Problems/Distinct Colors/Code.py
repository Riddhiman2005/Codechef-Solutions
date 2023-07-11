# Read the number of test cases
T = int(input())

# Iterate over each test case
for _ in range(T):
    # Read the number of colors
    N = int(input())

    # Read the counts of balls for each color
    counts = list(map(int, input().split()))

    # Find the maximum count
    max_count = max(counts)

    # Print the maximum count as the number of boxes needed
    print(max_count)
