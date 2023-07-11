
# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the values of a and b
    a, b = map(int, input().split())

    # Calculate the sum of a and b
    sum = a + b

    # Determine the winner based on the sum
    if sum % 2 == 0:
        winner = "Bob"
    else:
        winner = "Alice"

    # Print the winner
    print(winner)
