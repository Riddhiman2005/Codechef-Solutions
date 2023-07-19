def is_average_greater(a, b, c):
    average = (a + b) / 2
    return average > c

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    a, b, c = map(int, input().split())
    if is_average_greater(a, b, c):
        print("YES")
    else:
        print("NO")
