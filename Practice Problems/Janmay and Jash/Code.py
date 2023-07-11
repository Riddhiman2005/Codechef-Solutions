
# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the values of X and Y
    X, Y = map(int, input().split())

    # Determine the winner based on the parity of X and Y
    if (X + Y) % 2 == 0:
        print("Janmansh")
    else:
        print("Jay")
