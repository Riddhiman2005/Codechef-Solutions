
# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the bill amount
    x = int(input())

    # Calculate the maximum discount
    discount_1 = int(x * 0.1)  # 10% off
    discount_2 = 100  # Rs. 100 flat discount

    # Print the maximum discount
    print(max(discount_1, discount_2))
