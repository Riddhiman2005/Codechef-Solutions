# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the input values
    X, Y = map(int, input().split())

    # Calculate the maximum distance Chef can travel with the available fuel
    max_distance = X * 5

    # Compare the maximum distance with the distance to Chef's home and print the result
    if max_distance >= Y:
        print("YES")
    else:
        print("NO")
