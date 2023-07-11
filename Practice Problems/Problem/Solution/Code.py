
# Read the number of test cases, T
T = int(input())

# Iterate over each test case
for _ in range(T):
    # Read the initial number of problems of Alice, N, and the initial number of problems of Bob, M
    N, M = map(int, input().split())

    # Calculate the absolute difference between N and M
    diff = abs(N - M)

    # Check if the difference is divisible by 2 or 3
    if diff % 2 == 0 or diff % 3 == 0:
        print("YES")
    else:
        print("NO")
