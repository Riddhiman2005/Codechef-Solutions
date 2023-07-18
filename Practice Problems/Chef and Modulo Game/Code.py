# Function to calculate the maximum score for given (i, j, k)
def calculate_score(i, j, k, N):
    return (((N % i) % j) % k) % N

# Function to count the number of ways to obtain the maximum score
def count_ways(N, P):
    max_score = 0
    count = 0

    # Iterate over all possible combinations of (i, j, k)
    for i in range(1, P+1):
        for j in range(1, P+1):
            for k in range(1, P+1):
                score = calculate_score(i, j, k, N)
                if score > max_score:
                    max_score = score
                    count = 1
                elif score == max_score:
                    count += 1

    return count

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the input for each test case
    N, P = map(int, input().split())

    # Count the number of ways to obtain the maximum score
    result = count_ways(N, P)

    # Print the result
    print(result)
