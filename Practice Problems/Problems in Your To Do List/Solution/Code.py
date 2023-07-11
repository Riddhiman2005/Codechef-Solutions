
# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the number of problems in Chef's to-do list
    N = int(input())
    
    # Read the difficulty ratings of the problems
    ratings = list(map(int, input().split()))
    
    # Count the number of problems with difficulty rating >= 1000
    count = sum(1 for rating in ratings if rating >= 1000)
    
    # Print the number of problems to remove
    print(count)
