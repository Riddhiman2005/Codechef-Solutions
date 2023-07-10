
# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the age limits and Chef's age
    X, Y, A = map(int, input().split())

    # Check if Chef is eligible
    if A >= X and A < Y:
        print("YES")
    else:
        print("NO")
