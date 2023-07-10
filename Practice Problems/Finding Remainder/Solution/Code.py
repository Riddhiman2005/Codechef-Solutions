
# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the integers A and B
    a, b = map(int, input().split())

    # Find the remainder when A is divided by B
    remainder = a % b

    # Print the remainder
    print(remainder)
