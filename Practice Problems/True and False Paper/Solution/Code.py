
# Read the number of test cases, T
T = int(input())

# Iterate T times
for _ in range(T):
    # Read the values of N and K
    N, K = map(int, input().split())

    # Calculate the score of Bob
    Bob_score = N - K

    # Print the score of Bob
    print(Bob_score)
