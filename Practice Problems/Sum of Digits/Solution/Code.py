
# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the value of N
    N = int(input())

    # Calculate the sum of digits
    digit_sum = 0
    while N > 0:
        digit_sum += N % 10
        N //= 10

    # Print the sum of digits
    print(digit_sum)
