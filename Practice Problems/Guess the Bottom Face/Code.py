# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the value on the top face
    X = int(input())

    # Calculate the value on the bottom face
    bottom_face = 7 - X

    # Print the value on the bottom face
    print(bottom_face)
