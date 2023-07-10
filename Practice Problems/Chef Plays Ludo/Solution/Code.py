
# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the number rolled on the die
    X = int(input())

    # Check if Chef can enter a new token
    if X == 6:
        print("YES")
    else:
        print("NO")
