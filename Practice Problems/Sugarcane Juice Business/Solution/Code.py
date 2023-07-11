
# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the value of N
    N = int(input())

    # Calculate the juicer's profit
    income = N * 50
    expense_sugarcane = (20 * income) // 100
    expense_salt_mint = (20 * income) // 100
    expense_rent = (30 * income) // 100
    profit = income - expense_sugarcane - expense_salt_mint - expense_rent

    # Output the result
    print(profit)
