
# Read the number of test cases, T
T = int(input())

# Iterate T times
for _ in range(T):
    # Read the value of x
    x = int(input())

    # Calculate the price after discount
    selling_price = 100
    discount = int((x / 100) * selling_price)
    price = selling_price - discount

    # Print the price that Alice needs to pay
    print(price)
