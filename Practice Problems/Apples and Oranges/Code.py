def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Input
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    # Calculate the greatest common divisor (GCD) of N and M
    gcd_value = gcd(N, M)

    # Calculate the maximum number of contestants
    max_contestants = gcd_value

    # Print the result
    print(max_contestants)
