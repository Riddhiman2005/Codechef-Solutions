
# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the number of terms and the coefficients
    N = int(input())
    coefficients = list(map(int, input().split()))

    # Find the index of the last non-zero coefficient
    degree = -1
    for i in range(N):
        if coefficients[i] != 0:
            degree = i

    # Print the degree of the polynomial
    print(degree)
