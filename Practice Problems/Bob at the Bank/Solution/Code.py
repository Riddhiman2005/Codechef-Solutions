
# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the initial amount, deposit amount, deduction amount, and number of months
    w, x, y, z = map(int, input().split())

    # Calculate the final balance
    final_balance = w + (x * z) - (y * z)

    # Print the final balance
    print(final_balance)
