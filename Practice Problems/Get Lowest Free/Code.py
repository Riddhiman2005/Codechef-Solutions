# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the prices of the items
    A, B, C = map(int, input().split())

    # Find the minimum price among the three items
    min_price = min(A, B, C)

    # Calculate the total price paid by Chef
    total_price = A + B + C - min_price

    # Print the result
    print(total_price)
