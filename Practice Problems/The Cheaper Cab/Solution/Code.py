
# Read the number of test cases, T
T = int(input())

# Iterate T times
for _ in range(T):
    # Read the prices of the two cab services
    X, Y = map(int, input().split())

    # Compare the prices and determine the output
    if X < Y:
        print("FIRST")
    elif X > Y:
        print("SECOND")
    else:
        print("ANY")
