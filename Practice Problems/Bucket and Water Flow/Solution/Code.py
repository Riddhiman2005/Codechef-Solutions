
# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the input values
    w, x, y, z = map(int, input().split())

    # Calculate the final water level in the bucket
    final_water_level = w + (y * z)

    # Check if the bucket has overflown, filled exactly, or is still unfilled
    if final_water_level > x:
        print("overflow")
    elif final_water_level == x:
        print("filled")
    else:
        print("unfilled")
