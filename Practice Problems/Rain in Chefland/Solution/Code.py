
T = int(input())  # Read the number of test cases

for _ in range(T):
    X = int(input())  # Read the rate of rainfall in millimetre per hour

    if X < 3:
        print("LIGHT")  # Rainfall is less than 3 millimetre per hour
    elif X < 7:
        print("MODERATE")  # Rainfall is between 3 and 7 millimetre per hour
    else:
        print("HEAVY")  # Rainfall is greater than or equal to 7 millimetre per hour
