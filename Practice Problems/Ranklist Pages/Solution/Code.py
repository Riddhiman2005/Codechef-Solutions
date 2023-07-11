
# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read Chef's rank
    X = int(input())
    
    # Calculate the page number
    page_number = (X - 1) // 25 + 1
    
    # Print the page number
    print(page_number)

