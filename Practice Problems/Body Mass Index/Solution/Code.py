# Read the number of test cases

T = int(input())

# Process each test case
for _ in range(T):
    # Read the mass and height of Chef
    M, H = map(int, input().split())

    # Calculate the BMI
    BMI = M / (H ** 2)

    # Determine the category based on the BMI
    if BMI <= 18:
        print(1)  # Underweight
    elif 19 <= BMI <= 24:
        print(2)  # Normal weight
    elif 25 <= BMI <= 29:
        print(3)  # Overweight
    else:
        print(4)  # Obesity
