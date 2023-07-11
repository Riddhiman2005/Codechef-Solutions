
# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the durations of flight, bus, and train
    X, Y, Z = map(int, input().split())

    # Calculate the total time for each option
    plane_bus_time = X + Y
    train_time = Z

    # Compare the times and print the result
    if plane_bus_time < train_time:
        print("PLANEBUS")
    elif plane_bus_time > train_time:
        print("TRAIN")
    else:
        print("EQUAL")
