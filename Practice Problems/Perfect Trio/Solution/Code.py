
# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the ages of the three members
    A, B, C = map(int, input().split())

    # Check if the group is perfect
    if A == B + C or B == A + C or C == A + B:
        print("YES")
    else:
        print("NO")
