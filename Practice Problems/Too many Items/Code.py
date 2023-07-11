# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the number of items bought by Chef
    N = int(input())

    # Calculate the number of polybags needed
    polybags = N // 10

    # Check if there are remaining items
    if N % 10 != 0:
        polybags += 1

    # Print the minimum number of polybags required
    print(polybags)
