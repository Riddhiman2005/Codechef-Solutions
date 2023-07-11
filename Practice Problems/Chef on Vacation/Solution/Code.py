
# Read the number of test cases
T = int(input())

# Iterate over each test case
for _ in range(T):
    # Read the durations of the family trip, trip with friends, and vacation days
    X, Y, Z = map(int, input().split())

    # Calculate the total duration of the two trips
    total_duration = X + Y

    # Check if Chef can go on both trips
    if total_duration <= Z:
        answer = "YES"
    else:
        answer = "NO"

    # Print the answer
    print(answer)
