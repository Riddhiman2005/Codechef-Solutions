
# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the decisions of the referees
    r1, r2, r3, r4 = map(int, input().split())

    # Check if all referees agree that the ball is inside limits
    if r1 == r2 == r3 == r4 == 0:
        print("IN")
    else:
        print("OUT")
