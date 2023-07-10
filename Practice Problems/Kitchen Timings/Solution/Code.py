
# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read X and Y
    X, Y = map(int, input().split())

    # Calculate the number of hours Chef works
    hours_worked = (Y - X + 12) % 12

    # Print the result
    print(hours_worked)
