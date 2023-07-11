# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the values of X and Y
    X, Y = map(int, input().split())

    # Compare the travel times and output the result
    if X < Y:
        print("BIKE")
    elif X > Y:
        print("CAR")
    else:
        print("SAME")
