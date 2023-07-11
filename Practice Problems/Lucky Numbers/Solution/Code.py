
# Read the number of test cases
T = int(input())

# Iterate over each test case
for _ in range(T):
    # Read X
    X = str(input())

    # Check if X contains the digit 7
    if '7' in X:
        print("YES")
    else:
        print("NO")
