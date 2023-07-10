
# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the value of X
    x = int(input())
    
    # Calculate the final amount Chef needs to pay
    if x <= 100:
        final_amount = x
    elif x <= 1000:
        final_amount = x - 25
    elif x <= 5000:
        final_amount = x - 100
    else:
        final_amount = x - 500
    
    # Print the final amount
    print(final_amount)
