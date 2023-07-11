
# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the input for each test case
    A, B, C = map(int, input().split())

    # Find the maximum distance among the throws
    max_distance = max(A, B, C)

    # Print the final score
    print(max_distance)
