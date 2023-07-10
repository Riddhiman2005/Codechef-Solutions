# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the amount of water drank
    X = int(input())

    # Check if Chef followed the advice
    if X >= 2000:
        print("YES")
    else:
        print("NO")
