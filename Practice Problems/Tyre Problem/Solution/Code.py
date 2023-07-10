
# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the number of bikes and cars
    N, M = map(int, input().split())

    # Calculate the total number of tires
    total_tires = (N * 2) + (M * 4)

    # Print the result
    print(total_tires)
