
# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the number of 5-seaters and 7-seaters
    N, M = map(int, input().split())

    # Calculate the maximum number of people that can travel together
    max_people = (N * 5) + (M * 7)

    # Print the maximum number of people
    print(max_people)
