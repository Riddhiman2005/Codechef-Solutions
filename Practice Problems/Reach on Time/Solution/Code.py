
# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the time Chef left before reaching
    X = int(input())

    # Check if Chef will reach on time
    if X >= 30:
        print("YES")
    else:
        print("NO")
