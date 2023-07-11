# Read the number of test cases, T
T = int(input())

# Iterate T times
for _ in range(T):
    # Read the values of X, Y, and Z
    X, Y, Z = map(int, input().split())

    # Calculate the total amount of money Chef has
    total_money = (5 * X) + (10 * Y)

    # Calculate the maximum number of chocolates that can be bought
    max_chocolates = total_money // Z

    # Print the maximum number of chocolates
    print(max_chocolates)
