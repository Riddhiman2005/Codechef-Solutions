
# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the revenues of the three companies
    r1, r2, r3 = map(int, input().split())

    # Check if any company has a monopolistic advantage
    if r1 > r2 + r3 or r2 > r1 + r3 or r3 > r1 + r2:
        print("YES")
    else:
        print("NO")
