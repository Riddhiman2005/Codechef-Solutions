
# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read N and X
    N, X = map(int, input().split())

    # Calculate the remaining number of donations needed
    remaining_donations = N - X

    # Print the result
    print(remaining_donations)
