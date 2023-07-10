
# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the values of N, M, and K
    n, m, k = map(int, input().split())

    # Check if it is possible for all N friends to register
    if (m - k) >= n:
        print("Yes")
    else:
        print("No")
