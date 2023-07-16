# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the values
    N, M = map(int, input().split())

    # Check if it is possible to satisfy the conditions
    if N == 1 or M == 1 or (N*M) % 2 == 0:
        print("YES")
    else:
        print("NO")
