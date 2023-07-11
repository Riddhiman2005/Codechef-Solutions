
# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the values of N and X
    N, X = map(int, input().split())

    # Calculate the total bill
    total_bill = N * X

    # Check if the total bill is equivalent to a valid phone number
    if len(str(total_bill)) == 5 and total_bill > 0:
        print("YES")
    else:
        print("NO")
