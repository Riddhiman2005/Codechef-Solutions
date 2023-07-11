
# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the values for A, B, X, and Y
    A, B, X, Y = map(int, input().split())

    # Calculate the total power that can be generated from X grams of Helium-3
    total_power = X * Y

    # Check if the total power generated is sufficient for the required number of years
    if total_power >= A * B:
        print("YES")
    else:
        print("NO")
