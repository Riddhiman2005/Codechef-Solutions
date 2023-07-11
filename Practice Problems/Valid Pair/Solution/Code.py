# Read the sock colors
A, B, C = map(int, input().split())

# Check if any two sock colors are the same
if A == B or B == C or C == A:
    print("YES")
else:
    print("NO")
