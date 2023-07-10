
# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the times taken by Alice, Bob, and Charlie
    a, b, c = map(int, input().split())

    # Calculate the average speeds
    speed_a = 400 / a
    speed_b = 400 / b
    speed_c = 400 / c

    # Determine the person with the highest average speed
    if speed_a > speed_b and speed_a > speed_c:
        print("ALICE")
    elif speed_b > speed_a and speed_b > speed_c:
        print("BOB")
    else:
        print("CHARLIE")
