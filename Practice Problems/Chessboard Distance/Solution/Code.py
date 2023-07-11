
# Read the number of test cases
T = int(input())

# Iterate over each test case
for _ in range(T):
    # Read the values for X1, Y1, X2, Y2
    X1, Y1, X2, Y2 = map(int, input().split())

    # Calculate the chessboard distance
    distance = max(abs(X1 - X2), abs(Y1 - Y2))

    print(distance)
