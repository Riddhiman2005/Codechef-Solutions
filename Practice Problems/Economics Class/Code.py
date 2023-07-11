# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the input for each test case
    N = int(input())
    S = list(map(int, input().split()))
    D = list(map(int, input().split()))

    # Initialize a variable to count the number of equilibrium points
    equilibrium_points = 0

    # Check for equilibrium at each time point
    for i in range(N):
        if S[i] == D[i]:
            equilibrium_points += 1

    # Print the number of equilibrium points
    print(equilibrium_points)
