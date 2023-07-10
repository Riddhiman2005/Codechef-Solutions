
# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the values of X, Y, and Z
    x, y, z = map(int, input().split())

    # Check if Chef can go to the gym and have a trainer
    if x + y <= z:
        print(2)
    # Check if Chef can only go to the gym
    elif x <= z:
        print(1)
    # Otherwise, Chef can't even go to the gym
    else:
        print(0)
