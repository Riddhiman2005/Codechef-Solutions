
# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the input for each test case
    N, M = map(int, input().split())

    # Calculate the minimum number of votes Om requires
    min_votes = (M // 2) + 1

    # Print the minimum number of votes
    print(min_votes)
