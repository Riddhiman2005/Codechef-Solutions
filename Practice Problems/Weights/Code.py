def can_measure_weight(W, X, Y, Z):
    # If the target weight is equal to any of the individual weights, return YES
    if W == X or W == Y or W == Z:
        return "YES"
    
    # If the target weight is greater than the sum of any two individual weights,
    # then it is not possible to form the target weight using the given weights
    if W > X + Y or W > X + Z or W > Y + Z:
        return "NO"
    
    # If the target weight is greater than the sum of all three individual weights,
    # then it is not possible to form the target weight using any combination of the weights
    if W > X + Y + Z:
        return "NO"
    
    return "YES"

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    W, X, Y, Z = map(int, input().split())
    print(can_measure_weight(W, X, Y, Z))
