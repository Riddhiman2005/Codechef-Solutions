
import math

# Read the number of test cases
T = int(input())

# Iterate over each test case
for _ in range(T):
    # Read X and Y
    X, Y = map(int, input().split())

    # Calculate the minimum number of games
    games = math.ceil((Y - X) / 8)

    # Print the result
    print(games)
