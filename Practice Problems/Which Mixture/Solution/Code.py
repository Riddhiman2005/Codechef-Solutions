
# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the quantities of solid and liquid
    A, B = map(int, input().split())

    # Check the type of mixture
    if A > 0 and B > 0:
        print("Solution")
    elif B == 0:
        print("Solid")
    else:
        print("Liquid")
