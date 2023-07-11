
# Read the number of test cases
T = int(input())

# Iterate over each test case
for _ in range(T):
    # Read positions and speeds
    x1, x2, x3, v1, v2 = map(int, input().split())

    # Calculate the time to reach the bottle
    t_chef = (x3 - x1) / v1
    t_kefa = (x2 - x3) / v2

    # Compare the arrival times
    if t_chef < t_kefa:
        result = "Chef"
    elif t_kefa < t_chef:
        result = "Kefa"
    else:
        result = "Draw"

    # Print the result
    print(result)
