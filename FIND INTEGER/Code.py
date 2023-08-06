# Function to check if all digits of a number are pairwise different
def has_pairwise_different_digits(number):
    digits = set()
    while number > 0:
        digit = number % 10
        if digit in digits:
            return False
        digits.add(digit)
        number //= 10
    return True

# Function to find the smallest number Y with pairwise different digits that is greater than X
def find_smallest_number(X):
    Y = X + 1
    while not has_pairwise_different_digits(Y):
        Y += 1
    return Y


T = int(input())

=
for _ in range(T):
    # Read input value
    X = int(input())
    
    # Find and print the smallest number Y
    Y = find_smallest_number(X)
    print(Y)
