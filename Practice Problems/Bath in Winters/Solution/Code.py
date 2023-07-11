
# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the input for each test case
    X, Y = map(int, input().split())

    # Calculate the maximum number of people that can take bath
    max_people = X // (2 * Y)

    # Print the maximum number of people
    print(max_people)
