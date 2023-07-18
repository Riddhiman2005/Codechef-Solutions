
# Function to calculate the total time Chef has to spend on filling the various forms
def calculate_total_time(N, A, B, S):
    total_time = 0
    for i in range(N):
        if S[i] == '0':
            total_time += A
        else:
            total_time += B
    return total_time

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the input for each test case
    N, A, B = map(int, input().split())
    S = input()

    # Calculate the total time
    total_time = calculate_total_time(N, A, B, S)

    # Print the result
    print(total_time)
