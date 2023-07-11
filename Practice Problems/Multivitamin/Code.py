# Read the number of test cases

T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the input for each test case
    X, Y = map(int, input().split())

    # Check if Chef has enough tablets for the given days
    if Y >= X * 3:
        print("YES")
    else:
        print("NO")
