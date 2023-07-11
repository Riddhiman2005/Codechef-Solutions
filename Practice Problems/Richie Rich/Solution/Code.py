
# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the values of A, B, and X
    A, B, X = map(int, input().split())

    # Calculate the number of years required to reach the goal
    years = (B - A) // X

    # Print the answer
    print(years)
