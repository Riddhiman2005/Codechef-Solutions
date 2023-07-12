# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the number of mountains
    N = int(input())

    # Initialize the maximum height as 0
    max_height = 0

    # Iterate over the heights of the mountains
    for _ in range(N):
        height = int(input())
        max_height = max(max_height, height)

    # Print the height of the tallest mountain
    print(max_height)
