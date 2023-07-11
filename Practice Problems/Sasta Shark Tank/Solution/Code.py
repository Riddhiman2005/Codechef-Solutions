
# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the amounts offered by the investors
    A, B = map(int, input().split())
    
    # Calculate the valuations of the investors' offers
    valuation_1 = A * 10
    valuation_2 = B * 5
    
    # Compare the valuations and determine which offer to accept
    if valuation_1 > valuation_2:
        print("FIRST")
    elif valuation_2 > valuation_1:
        print("SECOND")
    else:
        print("ANY")
