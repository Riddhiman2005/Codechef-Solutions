

import math

# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the input for each test case
    N = int(input())

    # Calculate the minimum number of cars required
    cars_required = math.ceil(N / 4)

    # Print the result
    print(cars_required)
