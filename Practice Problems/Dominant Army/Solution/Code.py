
# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the number of soldiers in each army
    na, nb, nc = map(int, input().split())

    # Check if any army is dominant
    if na > nb + nc or nb > na + nc or nc > na + nb:
        print("YES")
    else:
        print("NO")
