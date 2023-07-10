
# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the scores in three subjects
    a, b, c = map(int, input().split())

    # Calculate the average scores of any two subjects
    avg_ab = (a + b) / 2
    avg_ac = (a + c) / 2
    avg_bc = (b + c) / 2

    # Check if any average score is less than 35
    if avg_ab < 35 or avg_ac < 35 or avg_bc < 35:
        print("FAIL")
    else:
        print("PASS")
