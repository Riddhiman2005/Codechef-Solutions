
# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the value of X
    x = int(input())

    # Calculate the time remaining until 10 PM
    time_remaining = 10 - x

    # Check if there is enough time to complete all assignments
    if time_remaining >= 3:
        print("Yes")
    else:
        print("No")
