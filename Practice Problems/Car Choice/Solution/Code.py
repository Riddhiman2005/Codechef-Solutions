
# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the input values
    x1, x2, y1, y2 = map(int, input().split())

    # Calculate the expenses for each car
    expenses_car1 = y1 / x1
    expenses_car2 = y2 / x2

    # Compare the expenses and print the result
    if expenses_car1 < expenses_car2:
        print("-1")  # Choose Car 1
    elif expenses_car1 > expenses_car2:
        print("1")  # Choose Car 2
    else:
        print("0")  # Same expenses for both cars
