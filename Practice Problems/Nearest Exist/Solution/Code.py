
# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the seat number
    X = int(input())
    
    # Determine the exit based on the seat number
    if X <= 50:
        print("LEFT")
    else:
        print("RIGHT")
