# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the values of N, X, and Y
    N, X, Y = map(int, input().split())

    # Calculate the number of cells under attack
    cells_in_row_column = (N - 1) * 2
    cells_in_diagonals = min(N - X, N - Y) + min(X - 1, Y - 1) + min(N - X, Y - 1) + min(X - 1, N - Y)
    cells_under_attack = cells_in_row_column + cells_in_diagonals

    print(cells_under_attack)
