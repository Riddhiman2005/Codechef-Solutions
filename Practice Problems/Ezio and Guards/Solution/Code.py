
# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the values of X and Y
    x, y = map(int, input().split())

    # Check if Ezio can manipulate all the guards
    if x >= y:
        result = "YES"
    else:
        result = "NO"

    # Print the result
    print(result)
