
import math

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the number to be tested
    N = int(input())

    # Check if the number is prime
    if is_prime(N):
        print("yes")
    else:
        print("no")
