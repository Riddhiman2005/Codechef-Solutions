
import math

# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the values of g and c
    g, c = map(int, input().split())

    # Calculate the smallest height using the given formula
    height = (c**2) // (2*g)

    # Print the smallest height
    print(height)
