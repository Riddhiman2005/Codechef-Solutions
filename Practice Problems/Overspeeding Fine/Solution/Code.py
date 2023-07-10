
T = int(input())  # Read the number of test cases

for _ in range(T):
    X = int(input())  # Read the speed of Chef's car

    if X <= 70:
        print("No Fine")  # No fine if the speed is less than or equal to 70
    elif X > 70 and X <= 100:
        print("Rs 500 Fine")  # Rs 500 fine if the speed is greater than 70 and less than or equal to 100
    else:
        print("Rs 2000 Fine")  # Rs 2000 fine if the speed is greater than 100
