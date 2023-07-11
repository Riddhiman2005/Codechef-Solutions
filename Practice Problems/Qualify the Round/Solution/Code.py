
# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the input for each test case
    X, A, B = map(int, input().split())

    # Calculate the total score
    total_score = (A * 1) + (B * 2)

    # Check if Chef qualifies or not
    if total_score >= X:
        print("Qualify")
    else:
        print("NotQualify")
