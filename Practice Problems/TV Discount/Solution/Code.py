
# Read the number of test cases
T = int(input())

# Iterate over each test case
for _ in range(T):
    # Read the parameters for each test case
    A, B, C, D = map(int, input().split())

    # Calculate the discounted prices
    price1 = A - C
    price2 = B - D

    # Compare the discounted prices and print the result
    if price1 < price2:
        print("First")
    elif price2 < price1:
        print("Second")
    else:
        print("Any")
