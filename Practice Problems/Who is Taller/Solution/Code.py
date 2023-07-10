
# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the heights of Alice and Bob
    X, Y = map(int, input().split())

    # Compare the heights and print the result
    if X > Y:
        print("A")
    else:
        print("B")
