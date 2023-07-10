
# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the number of problems in each category
    s, t, e = map(int, input().split())

    # Determine the most active role
    if s > t and s > e:
        print("Setter")
    elif t > s and t > e:
        print("Tester")
    else:
        print("Editorialist")
