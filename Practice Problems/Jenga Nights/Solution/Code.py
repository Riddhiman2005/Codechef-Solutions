# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the input for each test case
    N, X = map(int, input().split())

    # Check if the game is valid
    if X >= N and X % N == 0:
        print("YES")
    else:
        print("NO")
