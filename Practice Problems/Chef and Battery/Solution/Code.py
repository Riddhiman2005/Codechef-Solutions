# Read the number of test cases
T = int(input())

# Iterate over each test case
for _ in range(T):
    # Read the current battery level
    N = int(input())

    # Initialize the time
    time = 0

    # Simulate the charging and discharging process
    while N != 50:
        if N < 50:
            N += 2
        else:
            N -= 3
        time += 1

    # Print the minimum time to reach 50% battery level
    print(time)
