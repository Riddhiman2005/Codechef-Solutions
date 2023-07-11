# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the four angles of the quadrilateral
    A, B, C, D = map(int, input().split())

    # Check if the sum of opposite angles is 180 degrees
    if A + C == 180 and B + D == 180:
        print("YES")
    else:
        print("NO")
