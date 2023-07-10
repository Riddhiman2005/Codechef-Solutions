
# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the input values
    x, y = map(int, input().split())

    # Calculate the threshold time
    threshold_time = 1.07 * x

    # Check if Chef's finish time is within 107% of the fastest finish time
    if y <= threshold_time:
        print("YES")
    else:
        print("NO")
