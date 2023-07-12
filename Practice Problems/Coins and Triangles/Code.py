# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the number of gold coins
    N = int(input())

    # Initialize the maximum height to 0
    height = 0

    # Iterate over the rows until we have enough coins
    while N >= height + 1:
        height += 1
        N -= height

    # Print the maximum height of the triangle
    print(height)
