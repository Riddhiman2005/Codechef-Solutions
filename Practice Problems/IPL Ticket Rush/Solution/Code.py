
# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read N and M
    N, M = map(int, input().split())

    # Calculate the number of students who won't be able to book tickets
    no_tickets = max(0, N - M)

    # Print the result
    print(no_tickets)
