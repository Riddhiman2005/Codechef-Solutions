# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the number of credits
    X = int(input())

    # Check the conditions and print the semester type
    if X > 65:
        print("Overload")
    elif X < 35:
        print("Underload")
    else:
        print("Normal")
