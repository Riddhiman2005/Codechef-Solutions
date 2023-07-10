
# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the marks scored in the first and second attempt
    X, Y = map(int, input().split())

    # Calculate the final score as the maximum of the two attempts
    final_score = max(X, Y)

    # Print the final score
    print(final_score)
