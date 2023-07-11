
# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the time control values
    a, b = map(int, input().split())

    # Calculate the total time
    total_time = a + b

    # Determine the format based on the total time
    if total_time < 3:
        print(1)  # Bullet
    elif 3 <= total_time <= 10:
        print(2)  # Blitz
    elif 11 <= total_time <= 60:
        print(3)  # Rapid
    else:
        print(4)  # Classical
