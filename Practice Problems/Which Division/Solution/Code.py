
# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the input value
    R = int(input())

    # Check the rating and print the corresponding division
    if R >= 2000:
        print(1)
    elif R >= 1600:
        print(2)
    else:
        print(3)
