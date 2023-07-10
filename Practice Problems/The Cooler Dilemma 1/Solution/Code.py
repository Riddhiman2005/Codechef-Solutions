
# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the values of X, Y, and M
    x, y, m = map(int, input().split())

    # Calculate the total cost of renting the cooler
    rent_cost = x * m

    # Check if the cost of renting is less than the cost of purchasing
    if rent_cost < y:
        print("YES")
    else:
        print("NO")
