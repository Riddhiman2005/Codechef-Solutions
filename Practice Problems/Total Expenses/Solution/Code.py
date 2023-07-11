# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the quantity and price per item
    quantity, price = map(int, input().split())

    # Calculate the total expenses
    total_expenses = quantity * price

    # Apply the discount if quantity is more than 1000
    if quantity > 1000:
        discount = 0.1 * total_expenses
        total_expenses -= discount

    # Print the total expenses with 6 decimal places
    print("{:.6f}".format(total_expenses))
