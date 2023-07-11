
# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the number of problems submitted and approved
    x, y = map(int, input().split())

    # Calculate the percentage of problems approved
    approval_percentage = (y / x) * 100

    # Check if the approval percentage is at least 50%
    if approval_percentage >= 50:
        print("YES")
    else:
        print("NO")
