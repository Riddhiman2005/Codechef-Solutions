
# Read the number of test cases
T = int(input())

# Iterate over each test case
for _ in range(T):
    # Read the values for N, K, and M
    N, K, M = map(int, input().split())

    # Calculate the minimum number of bags
    bags = N // (K * M)
    if N % (K * M) != 0:
        bags += 1

    print(bags)
