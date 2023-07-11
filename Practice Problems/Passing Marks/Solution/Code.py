
# Read the number of test cases
T = int(input())

# Iterate over each test case
for _ in range(T):
    # Read the seven integers
    minA, minB, minC, Tmin, A, B, C = map(int, input().split())

    # Check if Chef passes the semester
    if A >= minA and B >= minB and C >= minC and A + B + C >= Tmin:
        print("YES")
    else:
        print("NO")
