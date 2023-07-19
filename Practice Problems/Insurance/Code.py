def calculate_rebate(X, Y):
    return min(X, Y)

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    X, Y = map(int, input().split())
    print(calculate_rebate(X, Y))
