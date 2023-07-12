# Function to calculate the digit sum of a number
def digitSum(num):
    return sum(map(int, str(num)))

# Read the value of T
T = int(input())

# Process each test case
for _ in range(T):
    # Read the value of N
    N = int(input())

    # Find the smallest integer X
    X = N + 1
    while digitSum(X) % 2 == digitSum(N) % 2:
        X += 1

    # Print the result
    print(X)
