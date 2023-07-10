
# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the number of friends, cost of each burger, and total money Chef has
    n, x, k = map(int, input().split())

    # Check if Chef has enough money to buy a burger for each friend
    if n * x <= k:
        print("YES")
    else:
        print("NO")
