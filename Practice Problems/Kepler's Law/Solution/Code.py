
# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the time periods and semimajor axes
    T1, T2, R1, R2 = map(int, input().split())

    # Calculate the ratio of (T^2 / R^3) for each planet
    ratio1 = T1**2 / R1**3
    ratio2 = T2**2 / R2**3

    # Check if the ratios are equal
    if ratio1 == ratio2:
        print("Yes")
    else:
        print("No")
