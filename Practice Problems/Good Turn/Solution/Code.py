
# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the dice numbers for Chef and Chefina
    X, Y = map(int, input().split())

    # Check if the sum is greater than 6
  
    if X + Y > 6:
        print("YES")
    else:
        print("NO")
