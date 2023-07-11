# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the three angles of the triangle
    A, B, C = map(int, input().split())

    # Check if the sum of angles is equal to 180
    if A + B + C == 180:
        print("YES")
    else:
        print("NO")
