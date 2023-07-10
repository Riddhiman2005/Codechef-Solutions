
# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the frequency of Chef's commands
    X = int(input())

    # Check if the frequency is within the range of binary's hearing
    if 67 <= X <= 45000:
        print("YES")
    else:
        print("NO")
