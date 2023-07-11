
# Function to compute the maximum path sum
def compute_max_path_sum(triangle):
    # Get the number of rows in the triangle
    rows = len(triangle)

    # Iterate through each row from bottom to top
    for i in range(rows-2, -1, -1):
        # Update each element with the maximum sum from the next row
        for j in range(i+1):
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])

    # Return the maximum sum at the top of the triangle
    return triangle[0][0]


# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the number of rows in the triangle
    N = int(input())

    # Read the triangle
    triangle = []
    for _ in range(N):
        row = list(map(int, input().split()))
        triangle.append(row)

    # Compute and print the maximum path sum
    max_sum = compute_max_path_sum(triangle)
    print(max_sum)
