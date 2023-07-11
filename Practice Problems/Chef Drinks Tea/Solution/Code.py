
# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the values of X, Y, and Z
    X, Y, Z = map(int, input().split())
    
    # Calculate the number of refills
    refills = X // Y
    
    # Calculate the total cost of refills
    cost = refills * Z
    
    # Check if there is any remaining tea
    if X % Y != 0:
        cost += Z
    
    # Print the minimum amount Chef has to pay
    print(cost)
