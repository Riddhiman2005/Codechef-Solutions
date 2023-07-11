
# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the initial and final scores
    A, B = map(int, input().split())
    C, D = map(int, input().split())

    # Check if it is possible to reach the final score
    if (C >= A and D >= B) and (C - A) % 2 == 0 and (D - B) % 2 == 0:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")
