
# Read the number of test cases, T
T = int(input())

# Iterate over each test case
for _ in range(T):
    # Read the height of Chef's son, X, and the minimum height required for the ride, H
    X, H = map(int, input().split())

    # Check if Chef's son can go on the ride
    if X >= H:
        print("YES")
    else:
        print("NO")
