
# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the values of X and Y
    x, y = map(int, input().split())

    # Calculate the total amount Chef made
    if y <= x:
        amount = y
    else:
        amount = x + 2 * (y - x)

    # Print the result
    print(amount)
