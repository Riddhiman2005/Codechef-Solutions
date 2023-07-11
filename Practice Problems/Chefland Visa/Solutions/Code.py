
# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the input values
    x1, x2, y1, y2, z1, z2 = map(int, input().split())

    # Check the criteria
    if x2 >= x1 and y2 >= y1 and z2 <= z1:
        print("YES")
    else:
        print("NO")
