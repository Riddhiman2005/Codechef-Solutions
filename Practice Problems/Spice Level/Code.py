# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the spice level of the item
    X = int(input())

    # Determine the category based on the spice level
    if X < 4:
        category = "MILD"
    elif X < 7:
        category = "MEDIUM"
    else:
        category = "HOT"

    # Print the category
    print(category)
