
import math

# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the input for each test case
    A, B = map(int, input().split())

    # Calculate the GCD using math.gcd() function
    gcd = math.gcd(A, B)

    # Calculate the LCM using the formula: LCM(A, B) = (A * B) / GCD(A, B)
    lcm = (A * B) // gcd

    # Print the GCD and LCM
    print(gcd, lcm)
