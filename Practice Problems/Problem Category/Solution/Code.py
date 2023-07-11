
# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the rating of the problem
    x = int(input())
    
    # Check the category of the problem
    if 1 <= x < 100:
        category = "Easy"
    elif 100 <= x < 200:
        category = "Medium"
    else:
        category = "Hard"
    
    # Print the category
    print(category)
