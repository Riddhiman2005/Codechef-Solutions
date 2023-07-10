
# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the number of friends and slices each friend wants
    n, x = map(int, input().split())

    # Calculate the minimum number of pizzas required
    min_pizzas = (n * x + 3) // 4

    # Output the minimum number of pizzas required
    print(min_pizzas)
