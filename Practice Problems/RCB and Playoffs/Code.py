# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the input for each test case
    X, Y, Z = map(int, input().split())

    # Calculate the maximum possible points RCB can earn with the remaining games
    max_possible_points = X + (Z * 2)

    # Check if the maximum possible points is greater than or equal to the required points
    if max_possible_points >= Y:
        print("YES")
    else:
        print("NO")
