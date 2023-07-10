
# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the target score and current score
    X, Y = map(int, input().split())

    # Calculate the remaining runs needed to win
    remaining_runs = X - Y

    # Print the remaining runs
    print(remaining_runs)
