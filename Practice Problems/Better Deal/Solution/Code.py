
# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the discount percentages of the first and second store
    A, B = map(int, input().split())
    
    # Calculate the final prices at both stores
    price_first_store = (100 - A) * 100
    price_second_store = (100 - B) * 200
    
    # Compare the final prices and print the result
    if price_first_store < price_second_store:
        print("FIRST")
    elif price_second_store < price_first_store:
        print("SECOND")
    else:
        print("BOTH")
