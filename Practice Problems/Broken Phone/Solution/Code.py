
# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the costs of repairing and buying
    X, Y = map(int, input().split())

    # Compare the costs
    if X < Y:
        result = "REPAIR"
    elif X > Y:
        result = "NEW PHONE"
    else:
        result = "ANY"

    # Print the result
    print(result)
