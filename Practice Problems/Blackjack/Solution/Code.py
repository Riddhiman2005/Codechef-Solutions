
# Read the number of test cases
T = int(input())

# Iterate over each test case
for _ in range(T):
    # Read the values for A and B
    A, B = map(int, input().split())

    # Calculate the third number
    C = 21 - (A + B)

    # Check if the third number is valid
    if 1 <= C <= 10:
        print(C)
    else:
        print(-1)
