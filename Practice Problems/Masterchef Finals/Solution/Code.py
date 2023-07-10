# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the current rank of Chef
    X = int(input())

    # Check if Chef made it to the top 10
    if X <= 10:
        print("YES")
    else:
        print("NO")
