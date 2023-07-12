# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the number of submissions
    N = int(input())

    # Initialize a list to store the maximum scores
    max_scores = [0] * 12

    # Iterate over the submissions
    for _ in range(N):
        # Read the problem number and the score
        p, s = map(int, input().split())

        # Update the maximum score for the corresponding problem
        max_scores[p] = max(max_scores[p], s)

    # Calculate the total score
    total_score = sum(max_scores[1:9])

    # Print the total score
    print(total_score)
