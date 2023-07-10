def calculate_account_balance(x, y):
    if x % 5 != 0 or x + 0.5 > y:
        return y
    return y - x - 0.5

# Read X and Y from input
x, y = map(float, input().split())

# Calculate and print the account balance
result = calculate_account_balance(x, y)
print("{:.2f}".format(result))
