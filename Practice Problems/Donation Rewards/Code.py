
# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the number of blood donations
    X = int(input())

    # Determine the badge based on the number of donations
    if X <= 3:
        badge = "BRONZE"
    elif X <= 6:
        badge = "SILVER"
    else:
        badge = "GOLD"

    # Print the badge
    print(badge)
