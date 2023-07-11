# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the input for each test case
    N, X = map(int, input().split())
    ages = list(map(int, input().split()))

    # Count the number of eligible voters
    eligible_voters = sum(age >= X for age in ages)

    # Print the result
    print(eligible_voters)
