
# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the values of A, B, and C
    a, b, c = map(int, input().split())

    # Check if there are two numbers with odd sum
    if (a + b) % 2 == 1 or (b + c) % 2 == 1 or (c + a) % 2 == 1:
        print("YES")
    else:
        print("NO")
