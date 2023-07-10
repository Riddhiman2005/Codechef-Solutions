def calculate_extra_water(k, x):
    return k - x

# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the bucket capacity and current water level
    k, x = map(int, input().split())

    # Calculate and print the maximum amount of extra water
    extra_water = calculate_extra_water(k, x)
    print(extra_water)
