T = int(input())  # Read the number of test cases

for _ in range(T):
    X = int(input())  # Read the speed of Chef's car

    if X <= 70:
        print("0")  # No fine if the speed is less than or equal to 70
    elif X > 70 and X <= 100:
        print("500")  # Rs 500 fine if the speed is greater than 70 and less than or equal to 100
    else:
        print("2000")  # Rs 2000 fine if the speed is greater than 100
