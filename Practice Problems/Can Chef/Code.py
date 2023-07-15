
# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the amount of petrol and distance
    X, Y = map(int, input().split())

    # Calculate the total distance to be covered
    total_distance = 2 * Y

    # Check if the total distance is within the petrol capacity
    if total_distance <= X * 15:
        print("YES")
    else:
        print("NO")
