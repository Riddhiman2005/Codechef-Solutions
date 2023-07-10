
# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the lengths of the sides
    a, b, c = map(int, input().split())

    # Check if the triangle is scalene
    if a != b and b != c and a != c:
        print("YES")
    else:
        print("NO")
