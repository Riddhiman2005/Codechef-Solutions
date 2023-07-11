
# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the value of N
    N = int(input())

    # Calculate the number of notebooks that can be made
    notebooks = (N * 1000) // 100

    # Output the result
    print(notebooks)
