
# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the battery level
    x = int(input())

    # Check if the battery level is 15% or below
    if x <= 15:
        print("Yes")
    else:
        print("No")
