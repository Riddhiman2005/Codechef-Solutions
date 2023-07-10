# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read X and Y
    X, Y = map(int, input().split())

    # Calculate the total expenditure for the month
    total_expenditure = Y * 30

    # Check if Akshat has enough money
    if X >= total_expenditure:
        print("YES")
    else:
        print("NO")
