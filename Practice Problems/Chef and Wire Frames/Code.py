# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the dimensions of the plate and the cost per cm
    N, M, X = map(int, input().split())

    # Calculate the perimeter of the plate
    perimeter = 2 * (N + M)

    # Calculate the cost of the wireframe
    cost = perimeter * X

    # Print the cost
    print(cost)
