
# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the input for each test case
    A, B = map(int, input().split())

    # Calculate the sum of A and B
    total = A + B

    # Determine the winner based on the sum
    if is_prime(total):
        winner = "Alice"
    else:
        winner = "Bob"

    # Print the winner
    print(winner)
