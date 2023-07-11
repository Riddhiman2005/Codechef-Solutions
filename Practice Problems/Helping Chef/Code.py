# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the value of N
    N = int(input())

    # Check if N is less than 10
    if N < 10:
        print("Thanks for helping Chef!")
    else:
        print("-1")
