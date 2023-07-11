
# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the value of k
    k = int(input())

    # Initialize Faizal's position
    position = 0

    # Calculate Faizal's position after k seconds
    for i in range(1, k+1):
        if i % 2 == 1:
            position += 3
        else:
            position -= 1

    # Print Faizal's position
    print(position)
