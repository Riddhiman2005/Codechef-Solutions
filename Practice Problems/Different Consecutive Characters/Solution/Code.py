
# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the length of the binary string
    N = int(input())

    # Read the binary string
    S = input()

    # Initialize the count of operations to 0
    operations = 0

    # Iterate through the string starting from the second character
    for i in range(1, N):
        # If the current character is the same as the previous character, increment the count of operations
        if S[i] == S[i-1]:
            operations += 1

    # Print the count of operations
    print(operations)
