
# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the values of X, Y, and Z
    X, Y, Z = map(int, input().split())
    
    # Check the conditions and print the result
    if Z % X == 0 and Z % Y == 0:
        print("ANY")
    elif Z % X == 0:
        print("CHICKEN")
    elif Z % Y == 0:
        print("DUCK")
    else:
        print("NONE")
